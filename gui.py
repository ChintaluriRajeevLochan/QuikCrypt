import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from threading import Thread
from encryption import encrypt_file, decrypt_file

# Base setup
BASE_DIR = os.path.join(os.path.expanduser("~"), "QuickCrypt")
ENCRYPTED_FOLDER = os.path.join(BASE_DIR, "encrypted_files")
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)

selected_file = None  # Global file path

# Initialize GUI
root = tk.Tk()
root.title("🔐 QuikCrypt - File Encryptor")
root.geometry("540x480")
root.configure(bg="#0e1117")  # Deep navy background
root.resizable(False, False)

show_password = tk.BooleanVar(value=False)

# ---------- Functions ----------

def select_file():
    global selected_file
    file_path = filedialog.askopenfilename()
    if file_path:
        selected_file = file_path
        file_label.config(text=os.path.basename(file_path))
        status_label.config(text="File selected.")

def toggle_password_visibility():
    password_entry.config(show="" if show_password.get() else "*")

def run_in_thread(func):
    # Run function in thread and manage progress bar visibility
    def thread_func():
        progress_bar.pack(pady=10)
        progress_bar.start(10)
        try:
            func()
        finally:
            progress_bar.stop()
            progress_bar.pack_forget()
    Thread(target=thread_func).start()

def encrypt_action_thread():
    password = password_entry.get()
    try:
        encrypted_path = encrypt_file(selected_file, password)
        messagebox.showinfo("Success", f"Encrypted:\n{encrypted_path}")
        status_label.config(text="Encryption successful.")
        password_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label.config(text="Encryption failed.")

def encrypt_action():
    if not selected_file:
        messagebox.showwarning("No File", "Please select a file to encrypt.")
        return

    password = password_entry.get()
    if not password:
        messagebox.showwarning("No Password", "Please enter a password.")
        return

    run_in_thread(encrypt_action_thread)

def decrypt_action_thread():
    password = password_entry.get()
    output_name = os.path.basename(selected_file).replace(".enc", "")
    output_path = os.path.join(BASE_DIR, output_name)
    try:
        decrypt_file(selected_file, output_path, password)
        messagebox.showinfo("Success", f"Decrypted:\n{output_path}")
        status_label.config(text="Decryption successful.")
        password_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Wrong password! Decryption failed.")
        status_label.config(text="Wrong password.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label.config(text="Decryption failed.")

def decrypt_action():
    if not selected_file:
        messagebox.showwarning("No File", "Please select an encrypted file.")
        return

    password = password_entry.get()
    if not password:
        messagebox.showwarning("No Password", "Please enter the password.")
        return

    run_in_thread(decrypt_action_thread)

# ---------- UI Layout ----------

# Title
tk.Label(root, text="🔐 QuikCrypt", font=("Consolas", 24, "bold"), bg="#0e1117", fg="#00bcd4").pack(pady=(25, 8))
tk.Label(root, text="Secure File Encryptor / Decryptor", font=("Consolas", 12),
         bg="#0e1117", fg="#cccccc").pack()

# File selection
tk.Button(root, text="📂  Select File", command=select_file,
          bg="#1e88e5", fg="white", font=("Consolas", 11, "bold"), width=25).pack(pady=20)

file_label = tk.Label(root, text="No file selected", bg="#0e1117", fg="#888888", font=("Consolas", 10))
file_label.pack()

# Password input
tk.Label(root, text="🔑 Password:", bg="#0e1117", fg="white", font=("Consolas", 12)).pack(pady=(25, 5))
password_entry = tk.Entry(root, show="*", width=32, font=("Consolas", 12), relief="flat", bg="#222831", fg="white", insertbackground="white")
password_entry.pack()

tk.Checkbutton(root, text="Show Password", variable=show_password, command=toggle_password_visibility,
               bg="#0e1117", fg="white", font=("Consolas", 10), selectcolor="#0e1117",
               activebackground="#0e1117", activeforeground="white").pack(pady=5)

# Progress bar (initially hidden)
progress_bar = ttk.Progressbar(root, mode='indeterminate', length=350)

# Action buttons
button_frame = tk.Frame(root, bg="#0e1117")
button_frame.pack(pady=25)

tk.Button(button_frame, text="🔐 Encrypt", command=encrypt_action,
          bg="#00bcd4", fg="white", font=("Consolas", 11, "bold"), width=16).grid(row=0, column=0, padx=15)

tk.Button(button_frame, text="🔓 Decrypt", command=decrypt_action,
          bg="#f44336", fg="white", font=("Consolas", 11, "bold"), width=16).grid(row=0, column=1, padx=15)

# Status bar
status_label = tk.Label(root, text="Ready.", bg="#0e1117", fg="#aaaaaa", font=("Consolas", 9), anchor="w")
status_label.pack(side="bottom", fill="x", pady=(10, 5), padx=10)

# Footer
tk.Label(root, text="Developed by Rajeev Lochan Chintaluri", bg="#1e1e1e", fg="white", font=("Segoe UI", 8)).pack(side="bottom", pady=5)


# ---------- Run ----------
root.mainloop()

# 🔐 QuikCrypt

QuikCrypt is a sleek and secure file encryption & decryption desktop application built using Python and Tkinter. It allows users to safely encrypt files with password-based AES encryption and decrypt them later with the same password — all through a clean and modern user interface.

---

## 🚀 Features

- 📂 **File Selection** — Easily choose files from your system for encryption/decryption.
- 🔐 **AES Encryption** — Encrypts files using the secure AES (Fernet) algorithm.
- 🔑 **Password Protection** — Each file is encrypted with a password provided by the user.
- 👁️ **Toggle Password Visibility** — Show/hide your password as you type.
- ✅ **Progress Indicator** — Visual progress bar during encryption/decryption.
- 🧹 **Clear Password** — Easily reset the password field.
- ❓ **Help Section** — Basic instructions included in the app.
- 🎨 **Modern UI** — A dark-themed interface with custom icons and fonts.
- 🧊 **Installer Ready** — Comes with a Windows installer using Inno Setup.

---

## 🖥️ Tech Stack

- **Frontend:** Python `Tkinter`
- **Backend:** `cryptography` library (Fernet AES)
- **Packaging:** `PyInstaller`
- **Installer:** `Inno Setup`

---

## 📦 Installation

### 🛠️ Run from Source (for developers)

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/QuikCrypt.git
   cd QuikCrypt
2.Install dependencies:

bash

pip install -r requirements.txt
3.Run the application:


bash
python gui.py

💾 Windows Installer
If you downloaded the QuikCryptInstaller.exe:

Double-click the installer

Follow the prompts to install QuikCrypt

Launch it from the Start Menu

Note: You may see a "Publisher cannot be verified" warning. This happens because the app is not signed with a trusted certificate. It's safe to continue if you downloaded it from a trusted source.

🔒 How Encryption Works
QuikCrypt uses the Fernet symmetric encryption algorithm under the hood.

A password entered by the user is used to derive a strong encryption key.

The file is encrypted and saved with a .enc extension.

During decryption, the same password is required to restore the original file.

📝 Folder Structure
bash
Copy
Edit
QUICKCRYPT/
├── gui.py                # Main application GUI
├── encryption.py         # Core encryption logic
├── utils.py              # Helper functions
├── requirements.txt      # Dependencies
├── lock.ico              # Custom icon for the app
├── Installer.iss         # Inno Setup script
├── README.md             # This file
├── encrypted_files/      # Encrypted output files
├── decrypted_files/      # Decrypted output files (if needed)
├── dist/                 # Folder containing built .exe
└── ...
🙋‍♂️ How to Use
Launch the app.

Click Select File and choose the file to encrypt or decrypt.

Enter a password. This password will be required again for decryption.

Click Encrypt or Decrypt depending on your goal.

View the resulting file in the generated location.

📌 Note
Ensure you remember the password used during encryption. There's no way to recover it otherwise.

Output files are saved inside the QuickCrypt/encrypted_files directory in your home folder.

👨‍💻 Developed By
Rajeev Lochan Chintaluri

If you found this project helpful or interesting, feel free to reach out or give a ⭐ on GitHub.


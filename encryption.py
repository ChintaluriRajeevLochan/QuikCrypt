from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import base64

# Main base directory
BASE_DIR = os.path.join(os.path.expanduser("~"), "QuickCrypt")
ENCRYPTED_FOLDER = os.path.join(BASE_DIR, "encrypted_files")
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)

def derive_key(password: str, salt: bytes) -> bytes:
    """Derives a Fernet-compatible key from password and salt."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(file_path, password):
    # Generate a new random salt for each file
    salt = os.urandom(16)
    key = derive_key(password, salt)
    f = Fernet(key)

    with open(file_path, 'rb') as file:
        original = file.read()

    encrypted = f.encrypt(original)

    # Save salt + encrypted data
    encrypted_filename = os.path.basename(file_path) + ".enc"
    encrypted_path = os.path.join(ENCRYPTED_FOLDER, encrypted_filename)

    with open(encrypted_path, 'wb') as enc_file:
        enc_file.write(salt + encrypted)  # prepend salt

    return encrypted_path

def decrypt_file(encrypted_path, output_path, password):
    with open(encrypted_path, 'rb') as file:
        data = file.read()

    salt = data[:16]
    encrypted_data = data[16:]

    key = derive_key(password, salt)
    f = Fernet(key)

    try:
        decrypted = f.decrypt(encrypted_data)
    except InvalidToken:
        raise ValueError("Wrong password or corrupted file.")

    with open(output_path, 'wb') as dec_file:
        dec_file.write(decrypted)

import os
import json
import hashlib
from tkinter import *
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
from datetime import datetime

META_FILE = "file_metadata.json"

# ---------- Utility Functions ----------

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    return open("key.key", "rb").read()

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# ---------- Encryption Logic ----------

def encrypt_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    key = generate_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)
    enc_file = file_path + ".enc"

    with open(enc_file, "wb") as file:
        file.write(encrypted)

    file_hash = calculate_hash(file_path)
    metadata = {
        "original_file": file_path,
        "encrypted_file": enc_file,
        "timestamp": datetime.now().isoformat(),
        "hash": file_hash
    }

    with open(META_FILE, "w") as meta:
        json.dump(metadata, meta, indent=4)

    messagebox.showinfo("Success", f"Encrypted and saved: {enc_file}\nKey saved as: key.key")

# ---------- Decryption Logic ----------

def decrypt_file():
    enc_file_path = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*.enc")])
    if not enc_file_path:
        return

    key = load_key()
    fernet = Fernet(key)

    with open(enc_file_path, "rb") as enc_file:
        encrypted = enc_file.read()

    try:
        decrypted = fernet.decrypt(encrypted)
    except Exception as e:
        messagebox.showerror("Error", "Decryption failed: Invalid key or corrupt file.")
        return

    output_file = enc_file_path.replace(".enc", "_decrypted")

    with open(output_file, "wb") as dec_file:
        dec_file.write(decrypted)

    hash_after = calculate_hash(output_file)

    with open(META_FILE) as meta:
        metadata = json.load(meta)

    if hash_after == metadata["hash"]:
        messagebox.showinfo("Success", f"Decrypted successfully!\nFile integrity verified ✅\nSaved as: {output_file}")
    else:
        messagebox.showwarning("Warning", f"Decrypted, but integrity check FAILED ⚠\nSaved as: {output_file}")

# ---------- GUI Setup ----------

app = Tk()
app.title("Secure File Storage with AES")
app.geometry("400x250")
app.resizable(False, False)

Label(app, text="Secure File Storage System", font=("Arial", 16)).pack(pady=20)

Button(app, text="Encrypt File", command=encrypt_file, width=20, bg="green", fg="white").pack(pady=10)
Button(app, text="Decrypt File", command=decrypt_file, width=20, bg="blue", fg="white").pack(pady=10)

Label(app, text="AES Encryption • Fernet • SHA-256 Integrity", font=("Arial", 9)).pack(side="bottom", pady=10)

app.mainloop()

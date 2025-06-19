# 🔐 Secure File Storage System with AES Encryption

This project is a secure file storage system that allows users to encrypt and decrypt files using AES-256 encryption. It also includes integrity verification using SHA-256 hash and provides a user-friendly GUI built with Tkinter.

## 🚀 Features

- AES-256 file encryption and decryption using `cryptography` (Fernet)
- GUI interface using Tkinter (Encrypt / Decrypt with buttons)
- Automatic SHA-256 hash verification on decryption
- Secure key generation and storage
- Metadata logging (original file name, hash, timestamp) in JSON

## 📦 Requirements

- Python 3.x
- `cryptography`
- `hashlib`
- `tkinter` (comes with Python)
- `json` (built-in)

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yamish67/Intership/blob/main/Projects/
   cd Projects
   ```

2. Install dependencies:
   ```bash
   pip install cryptography
   ```

3. Run the GUI OR EXECUTABLE(.exe):
   ```bash
   python secure_file_storage_gui.py
   
   secure_file_storage_gui.exe  # for running .exe
   ```

## 💡 How It Works

1. **Encrypt File**: Select any file. It will be encrypted using a new AES key. A `.enc` file is created, and the key is saved as `key.key`.
2. **Decrypt File**: Select the `.enc` file. The app uses the saved key to decrypt and checks file integrity using SHA-256.
3. **Metadata**: Stored in `file_metadata.json` — includes filename, hash, and timestamp.

## 📄 Report

A 2-page project report is available in this repository: `Secure_File_Storage_AES_Report.pdf`

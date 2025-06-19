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
   git clone https://github.com/your-username/secure-file-storage-aes.git
   cd secure-file-storage-aes

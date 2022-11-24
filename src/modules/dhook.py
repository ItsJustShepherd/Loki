# Imports.
import sys # System stuff.
import os # Operating System functions.
from colorama import Fore # For text colour.
from dhooks import Webhook, File
from io import BytesIO

# Pre-run.
# os.system("clear")

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
def hook():
    try:
        print(f"\n{print_alert} Files uploaded to Discord will be kept on their servers according to ToS.\nYour IP and traffic may also be logged when using Discord.\n\n{print_prompt} Currently only sends the loki.key to Discord.") # \nWhen it comes to sFTP/scp the file will be encrypted with loki+zipped before\nsending using a key called 'hook.key'.  This new key is also sent.")
        print(f"\n{print_question} Will you be hooking to [Discord]") # [../sFTP/scp] in next update.
        option = input(f"{print_command}") # Prompts for command input.
        hook_url = input(f"\n{print_prompt} Specify your hook url: ") # Prompts for hook url input.

        hook = Webhook(f'{hook_url}')

        hook_message = input(f"\n{print_prompt} Specify your hook message: ") # Prompts for message input.

        file_name = input(f"\n{print_prompt} Specify file name on upload: ") # Prompts for file name input.

        file = File('loki.key', name=f'{file_name}')  # optional name for discord.

        hook.send(f'{hook_message}:', file=file) # sends loki.key file.
        
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
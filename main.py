# NemogeN - Random Emoticon / Emoji Generator
# Author: Nikos-Nikitas
# GitHub: https://github.com/nikosnikitas

import random
import sys
import time

''' Helper function - Getting only an integer number from input. '''
def get_int(message=" Enter an integer number: "):
    try:
        n = int(input(message))
        if n == 0:
            raise ValueError
        else:
            return n
    except ValueError:
        print("-- VALUE ERROR: Please enter an integer number except 0. --")
        time.sleep(0.3)
        return get_int()


''' Generating a random emoticon/emoji from unicode characters (UTF-8).
    Combining ANSI color codes for the terminal. '''
def generate_emoji():

    emojis = ["\U0001F600", "\U0001F601", "\U0001F602", "\U0001F603"]

    n = get_int(message="\033[0;37mHow many emojis to generate? ")

    for i in range(n):
        random.shuffle(emojis)
        emoji = random.choice(emojis)
        sys.stdout.write(f"\033[1;33m{emoji} ")
    print("")


''' The help menu for available options. '''
def display_help():
    print("[ -- NemogeN Help Menu -- ]")
    print("[OPTION] : [DESCRIPTION]")
    print("-h / help / [NO OPTION] : Display this help menu.")
    print("-c / cli : Command Line Interface (CLI) Mode.")
    print("-e / emoji : Generate an emoji instantly.")
    sys.exit()


''' Starting in Command Line Interface (CLI) Mode. '''
def cli_mode():
    print("[ -- NemogeN -- ]")
    print("[ -- Author: Nikos-Nikitas -- ]")
    print("[ -- GitHub: https://github.com/nikosnikitas -- ]")
    print("""Hello! This is a random emoji generator.
            \033[0;32m\U0001F600""", end="\n")
    generate_emoji()
    sys.exit()


''' Comparing given options to the available options. '''
def check_args():
    options = ['-h', '-c', '-e', 'help', 'cli']
    try:
        if sys.argv[1] in options:

            if (len(sys.argv) > 2) and (sys.argv[1] not in options):
                print("Too many options added.")
                sys.exit()
            elif len(sys.argv) < 2:
                return
            elif (sys.argv[1] == "-h" or sys.argv[1] == "help"):
                display_help()
            elif (sys.argv[1] == "-e") or (sys.argv[1] == "emoji"):
                generate_emoji()
            elif (sys.argv[1] == "-c") or (sys.argv[1] == "cli"):
                cli_mode()
            else:
                check_args()
        else:
            display_help()
    except IndexError:
        display_help()


''' Main program loop calls to check the arguments / options on start. '''
def main():
    check_args()

if __name__ == '__main__':
    main()
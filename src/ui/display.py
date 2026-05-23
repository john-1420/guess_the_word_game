# Display functions and colour handling
from colorama import Fore, Style, init
init(autoreset=True)

# Colour constants
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
RESET = Style.RESET_ALL

def apply_color(text, color, config):
    """Apply colour only if colour_output is enabled."""
    if config.get("colour_output", True):
        return f"{color}{text}{RESET}"
    return text

#This function prints the updated word after the guess has been made
def update_display(word_display, config):
    """
    Display the current state of the word to the user.
    """
    text = " ".join(word_display)
    print(apply_color("\n" + text, CYAN, config))
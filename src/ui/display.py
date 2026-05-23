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
    """
    Apply colour formatting to text if colour output is enabled.

    Parameters:
        text (str): The text to colour.
        color (str): A colorama colour constant (e.g., Fore.GREEN).
        config (dict): Configuration settings, used to check if colour_output is enabled.

    Returns:
        str: The coloured text if enabled, otherwise the original text.
    """
    if config.get("colour_output", True):
        return f"{color}{text}{RESET}"
    return text


def update_display(word_display, config):
    """
    Print the current state of the word being guessed.

    Parameters:
        word_display (list[str]): A list of characters and underscores representing the word state.
        config (dict): Configuration settings for colour output.

    Returns:
        None
    """
    text = " ".join(word_display)
    print(apply_color("\n" + text, CYAN, config))
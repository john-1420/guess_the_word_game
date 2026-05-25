# Menus: main menu, settings menu, high score display

from .display import apply_color, CYAN, MAGENTA, YELLOW, GREEN
from src.persistence.highscores import load_highscores
from src.config_manager import save_config


def main_menu(config):
    """
    Display the main menu and prompt the user to choose an option.

    Parameters:
        config (dict): Configuration settings used for colour output.

    Returns:
        str: The selected menu option ("1", "2", "3", or "4").
    """
    print(apply_color("\nMAIN MENU", CYAN, config))
    print(apply_color("[1] Play Game", MAGENTA, config))
    print(apply_color("[2] View High Scores", MAGENTA, config))
    print(apply_color("[3] Settings", MAGENTA, config))
    print(apply_color("[4] Exit", MAGENTA, config))

    while True:
        choice = input("Choose an option: ").strip()
        if choice in ["1", "2", "3", "4"]:
            return choice
        print(apply_color("Invalid choice.", YELLOW, config))


def display_highscores(config):
    """
    Display the list of saved high scores.

    Parameters:
        config (dict): Configuration settings for colour output.

    Returns:
        None
    """
    data = load_highscores()

    print(apply_color("\n=== HIGH SCORES ===", CYAN, config))
    if not data["scores"]:
        print(apply_color("No high scores yet.", YELLOW, config))
        return

    for i, entry in enumerate(data["scores"], start=1):
        line = f"{i}. {entry['name']} - {entry['score']} pts ({entry['date']})"
        print(apply_color(line, MAGENTA, config))


def settings_menu(config):
    """
    Display and manage the settings menu.

    Allows the user to:
        - Toggle colour output
        - Toggle logging level (INFO/DEBUG)
        - Save changes
        - Cancel changes

    Parameters:
        config (dict): The current configuration settings.

    Returns:
        None
    """
    while True:
        print(apply_color("\n=== SETTINGS ===", CYAN, config))
        print(apply_color(f"[1] Toggle Colour Mode (currently: {config['colour_output']})", MAGENTA, config))
        print(apply_color(f"[2] Toggle Logging Level (currently: {config['logging_level']})", MAGENTA, config))
        print(apply_color("[3] Save & Return", MAGENTA, config))
        print(apply_color("[4] Cancel", MAGENTA, config))

        choice = input("Choose an option: ").strip()

        if choice == "1":
            config["colour_output"] = not config["colour_output"]
            print(apply_color(f"Colour mode set to {config['colour_output']}", GREEN, config))

        elif choice == "2":
            config["logging_level"] = "DEBUG" if config["logging_level"] == "INFO" else "INFO"
            print(apply_color(f"Logging level set to {config['logging_level']}", GREEN, config))

        elif choice == "3":
            save_config(config)
            print(apply_color("Settings saved!", GREEN, config))
            return

        elif choice == "4":
            print(apply_color("Changes discarded.", YELLOW, config))
            return

        else:
            print(apply_color("Invalid choice.", YELLOW, config))
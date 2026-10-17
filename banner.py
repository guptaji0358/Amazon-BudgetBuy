import os
import shutil
from colorama import Fore, Style

Version = "v2.0"

# ===================== ASCII LOGO =====================
Logo = [
    "█▄▄ █ █ █▀▄ █▀▀ █▀▀ ▀█▀   █▄▄ █ █ █▄█",
    "█▄█ █▄█ █▄▀ █▄█ ██▄  █    █▄█ █▄█  █ ",
]


def ClearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def _Row(Text, Width, Color=""):
    """One boxed line, padded so the right border stays aligned."""
    return Fore.CYAN + "│ " + Color + Text.ljust(Width - 4) + Fore.CYAN + " │"


def ShowBanner(SettingsData, Platforms):
    """Static welcome panel (Claude Code / OpenCode style). Clears the screen first."""
    ClearScreen()
    Width = min(max(shutil.get_terminal_size((80, 20)).columns - 2, 60), 72)
    Title = f" Budget Buy {Version} "
    Bar = "─" * (Width - 3 - len(Title))

    print(Fore.CYAN + "╭─" + Style.BRIGHT + Fore.YELLOW + Title + Style.RESET_ALL + Fore.CYAN + Bar + "╮")
    print(_Row("", Width))
    for Line in Logo:
        print(_Row(Line, Width, Style.BRIGHT + Fore.YELLOW))
    print(_Row("", Width))
    print(_Row("Multi-Platform Price Tracker", Width, Style.BRIGHT + Fore.WHITE))
    print(_Row("", Width))
    print(_Row(f"Platforms : {', '.join(Platforms)}", Width, Fore.GREEN))
    print(_Row(f"Email     : {SettingsData['EmailMode']}", Width, Fore.GREEN))
    print(_Row(f"Directory : {os.path.basename(os.getcwd())}", Width, Fore.GREEN))
    print(_Row("", Width))
    print(_Row("Tips: paste a product URL to start  ·  'S' settings", Width, Style.DIM + Fore.WHITE))
    print(Fore.CYAN + "╰" + "─" * (Width - 2) + "╯" + Style.RESET_ALL)

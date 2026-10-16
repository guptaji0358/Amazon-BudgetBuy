import json
import os
from colorama import Fore, Style

SettingsFilePath = os.path.join(os.path.dirname(__file__), "settings.json")

# ===================== EMAIL SEND MODES =====================
EmailMode_Auto = "AUTO"    # Send automatically, no confirmation
EmailMode_Ask = "ASK"      # Ask Y/N every time before sending
EmailMode_Never = "NEVER"  # Never send email alerts

DefaultSettings = {
    "UserGmail": "",
    "UserPassword": "",
    "ReceiverMail": "",
    "EmailMode": EmailMode_Ask,
}


def LoadSettings():
    if not os.path.exists(SettingsFilePath):
        return None

    with open(SettingsFilePath, "r", encoding="utf-8") as SettingsFile:
        return json.load(SettingsFile)


def SaveSettings(SettingsData):
    with open(SettingsFilePath, "w", encoding="utf-8") as SettingsFile:
        json.dump(SettingsData, SettingsFile, indent=4)


def ConfigureEmailSettings(ExistingSettings=None):
    """Interactive setup/edit of email credentials & send mode."""
    SettingsData = dict(ExistingSettings) if ExistingSettings else dict(DefaultSettings)

    print(Fore.CYAN + "\n" + "=" * 65)
    print(Style.BRIGHT + Fore.YELLOW + "📧 EMAIL CONFIGURATION")
    print(Fore.CYAN + "=" * 65)

    SettingsData["UserGmail"] = input(
        Fore.GREEN + f"Gmail Address [{SettingsData['UserGmail'] or 'none'}]: "
    ).strip() or SettingsData["UserGmail"]

    SettingsData["UserPassword"] = input(
        Fore.GREEN + "Gmail App Password (leave blank to keep existing): "
    ).strip() or SettingsData["UserPassword"]

    SettingsData["ReceiverMail"] = input(
        Fore.GREEN + f"Receiver Email [{SettingsData['ReceiverMail'] or 'none'}]: "
    ).strip() or SettingsData["ReceiverMail"]

    # ===================== EMAIL SEND MODE =====================
    print(Fore.CYAN + "\nWhen Your Target Price Is Hit, Should An Email Be Sent?")
    print(Fore.GREEN + "  1) Auto     - Send Automatically, No Confirmation")
    print(Fore.GREEN + "  2) Ask      - Ask Y/N Every Time")
    print(Fore.GREEN + "  3) Never    - Don't Send Any Email")

    ModeChoice = input(Fore.GREEN + "Choose [1/2/3]: ").strip()
    ModeMap = {"1": EmailMode_Auto, "2": EmailMode_Ask, "3": EmailMode_Never}
    SettingsData["EmailMode"] = ModeMap.get(ModeChoice, SettingsData["EmailMode"])

    SaveSettings(SettingsData)
    print(Fore.GREEN + Style.BRIGHT + "\n✅ Settings Saved Successfully!")

    return SettingsData


def GetOrCreateSettings():
    """Loads settings, or walks the user through first-time setup."""
    SettingsData = LoadSettings()

    if SettingsData is None:
        print(Fore.YELLOW + "\n⚠ No Email Configuration Found. Let's Set It Up.")
        SettingsData = ConfigureEmailSettings()

    return SettingsData

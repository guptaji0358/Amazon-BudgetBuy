#Project - Budget Buy (Multi-Platform Price Tracker)
# --------------------------
import time
from colorama import Fore, Style, init

from scrapers import GetScraperForURL, SupportedPlatforms
from email_alert import SendPriceAlert
from display import ShowProductDetails
from settings import GetOrCreateSettings, ConfigureEmailSettings, EmailMode_Auto, EmailMode_Ask, EmailMode_Never

# ===================== INITIALIZE COLORAMA =====================
init(autoreset=True)

# ===================== LOAD / FIRST-TIME EMAIL SETUP =====================
SettingsData = GetOrCreateSettings()

# ===================== MAIN LOOP =====================
Replay = True
while Replay:

    # ===================== HEADER =====================
    print(Fore.CYAN + "=" * 65)
    print(Style.BRIGHT + Fore.YELLOW + "🛒 BUDGET BUY - PRICE TRACKER")
    print(Fore.CYAN + f"Supported Platforms: {', '.join(SupportedPlatforms())}")
    print(Fore.CYAN + f"📧 Email Mode: {SettingsData['EmailMode']}  (Type 'S' Below To Change)")
    print(Fore.CYAN + "=" * 65)

    # ===================== URL INPUT =====================
    while True:
        ProductURL = input(Fore.GREEN + "\n🔗 Paste Product URL (Or 'S' For Settings):\n").strip()

        if ProductURL.lower() in ["s", "settings"]:
            SettingsData = ConfigureEmailSettings(SettingsData)
            continue

        if ProductURL.startswith("http://") or ProductURL.startswith("https://"):
            ScraperInstance = GetScraperForURL(ProductURL)
            break
        else:
            print(Fore.RED + "\n❌ Invalid URL! Try Again.\n")

    # ===================== TARGET PRICE =====================
    while True:
        try:
            TargetPrice = float(input(Fore.GREEN + "\n💰 Enter Your Target Price ₹:\n"))
            break
        except ValueError:
            print(Fore.RED + "❌ Please Enter Numbers Only!")

    # ===================== FETCH PRODUCT =====================
    try:
        Mode = ScraperInstance.Name if ScraperInstance.Name != "Generic" else "Generic (Auto-Detect)"
        print(Fore.YELLOW + f"\n⏳ Fetching Product Details Using {Mode} Scraper...")
        ProductDetails = ScraperInstance.GetProductDetails(ProductURL)

    except Exception as error:
        print(Fore.RED + f"\n❌ Request Failed: {error}")
        continue

    # ===================== VALIDATION =====================
    if not ProductDetails:
        print(Fore.RED + "\n❌ Failed To Fetch Product Details")
        print(Fore.YELLOW + "⚠ The Site May Be Blocking Requests Or Changed Its Layout.")
        continue

    ProductTitle = ProductDetails["Title"]
    PriceText = ProductDetails["PriceText"]
    CurrentPrice = ProductDetails["Price"]

    # ===================== SHOW PRODUCT =====================
    ShowProductDetails(ProductDetails, TargetPrice)

    # ===================== PRICE CHECK =====================
    if CurrentPrice <= TargetPrice:
        print(Style.BRIGHT + Fore.GREEN + "\n🎉 Product Is Within Your Budget!")

        # ===================== DECIDE WHETHER TO SEND EMAIL =====================
        EmailMode = SettingsData["EmailMode"]

        if EmailMode == EmailMode_Never:
            ShouldSendEmail = False
            print(Fore.YELLOW + "✋ Email Alerts Are Turned Off (Settings → Never).")

        elif EmailMode == EmailMode_Auto:
            ShouldSendEmail = True

        else:  # EmailMode_Ask
            Answer = input(Fore.CYAN + "📧 Send Email Alert For This Product? (Y/N): ").strip().lower()
            ShouldSendEmail = Answer in ["y", "yes"]

        # ===================== SEND EMAIL =====================
        if ShouldSendEmail:
            try:
                SendPriceAlert(SettingsData, ProductTitle, PriceText, ProductURL)
                print(Fore.GREEN + "📧 Email Alert Sent Successfully!")

            except Exception as error:
                print(Fore.RED + f"❌ Email Failed: {error}")
        else:
            print(Fore.YELLOW + "📭 Email Alert Skipped.")
    else:
        Difference = CurrentPrice - TargetPrice
        print(Style.BRIGHT + Fore.RED + f"\n❌ Still Expensive By ₹{Difference:.2f}")

    # ===================== CONTINUE / EXIT =====================
    while True:
        Ask = input(Fore.CYAN + "\nDo You Want To Check Another Product?\n"
                               "👉 Type 'C' or 'Continue'\n""👉 Type 'E' or 'Exit'\n\n").lower()

        # ===================== EXIT =====================
        if Ask in ["e", "exit"]:
            print(Fore.YELLOW + "\n⏳ Exiting Application...")
            time.sleep(2)
            print(Style.BRIGHT + Fore.GREEN + "🙏 Thank You For Using Budget Buy")
            Replay = False
            break

        # ===================== CONTINUE =====================
        elif Ask in ["c", "continue"]:
            print(Fore.GREEN + "\n🔄 Restarting Application...\n")
            time.sleep(1)
            break

        # ===================== INVALID =====================
        else:
            print(Fore.RED + "\n❌ Invalid Input! Try Again.")

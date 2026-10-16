from colorama import Fore, Style

# ===================== AUTHENTICITY BADGES =====================
AuthenticityBadges = {
    "OFFICIAL": (Fore.GREEN, "✅ OFFICIAL / BRAND SOLD"),
    "THIRD_PARTY": (Fore.YELLOW, "⚠️ THIRD-PARTY SELLER"),
    "UNKNOWN": (Fore.RED, "❓ COULD NOT VERIFY"),
}


def ShowProductDetails(ProductDetails, TargetPrice):
    Authenticity = ProductDetails["Authenticity"]
    BadgeColor, BadgeText = AuthenticityBadges[Authenticity["Status"]]

    print(Fore.CYAN + "\n" + "═" * 65)
    print(Style.BRIGHT + Fore.GREEN + f"📦 Product:\n{ProductDetails['Title']}")

    print(Fore.CYAN + "-" * 65)
    print(Fore.YELLOW + f"💰 Current Price : {ProductDetails['PriceText']}")
    print(Fore.MAGENTA + f"🎯 Target Price  : ₹{TargetPrice}")
    print(Fore.BLUE + f"🏬 Platform      : {ProductDetails['Platform']}")
    print(Fore.BLUE + f"🧾 Seller        : {Authenticity['SellerName']}")

    print(Fore.CYAN + "-" * 65)
    print(BadgeColor + Style.BRIGHT + f"🛡️  Authenticity : {BadgeText}")
    print(BadgeColor + f"    Reason      : {Authenticity['Reason']}")

    if not Authenticity["Secure"]:
        print(Fore.RED + "    ⚠ Site Is Not Using HTTPS — Be Cautious!")

    print(Fore.CYAN + "═" * 65)

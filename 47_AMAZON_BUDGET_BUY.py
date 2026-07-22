#Project - Amazon Buget Buy
# --------------------------
import requests
from bs4 import BeautifulSoup
import smtplib
import time
from colorama import Fore, Style, init

# ===================== INITIALIZE COLORAMA =====================
init(autoreset=True)

# ===================== USER DATA =====================
UserGmail = "YOUR_GMAIL@gmail.com"
UserPassword = "YOUR_APP_PASSWORD"
ReceiverMail = "RECEIVER@gmail.com"

# ===================== HEADERS =====================
Headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120 Safari/537.36"
    ),
    "Accept-Language": "en-IN,en;q=0.9",
}

# ===================== MAIN LOOP =====================
Replay = True
while Replay:

    # ===================== HEADER =====================
    print(Fore.CYAN + "=" * 65)
    print(Style.BRIGHT + Fore.YELLOW + "🛒 AMAZON PRICE TRACKER")
    print(Fore.CYAN + "=" * 65)

    # ===================== URL INPUT =====================
    while True:
        ProductURL = input(Fore.GREEN +"\n🔗 Paste Amazon Product URL:\n").strip()

        if ProductURL.startswith("https://www.amazon.in"):
            break

        else:
            print(Fore.RED +"\n❌ Invalid Amazon URL! Try Again.\n")

    # ===================== TARGET PRICE =====================
    while True:
        try:
            TargetPrice = float(input(Fore.GREEN +"\n💰 Enter Your Target Price ₹:\n"))
            break
        except ValueError:
            print(Fore.RED +"❌ Please Enter Numbers Only!")

    # ===================== FETCH PRODUCT =====================
    try:
        print(Fore.YELLOW +"\n⏳ Fetching Product Details...")
        Response = requests.get(ProductURL, headers=Headers)

        print(Fore.CYAN +f"🌐 Status Code: {Response.status_code}")
        Soup = BeautifulSoup(Response.text, "html.parser")

    except Exception as error:
        print(Fore.RED +f"\n❌ Request Failed: {error}")
        continue

    # ===================== EXTRACT TITLE =====================
    TitleElement = Soup.find(id="productTitle")

    # ===================== EXTRACT PRICE =====================
    PriceElement = Soup.select_one(".a-price .a-offscreen")

    # ===================== VALIDATION =====================
    if not TitleElement or not PriceElement:
        print(Fore.RED +"\n❌ Failed To Fetch Product Details")
        print(Fore.YELLOW +"⚠ Amazon may be blocking requests.")
        continue

    # ===================== CLEAN TITLE =====================
    ProductTitle = TitleElement.get_text().strip()

    # ===================== CLEAN PRICE =====================
    PriceText = PriceElement.get_text().strip()
    CleanPrice = (PriceText.replace("₹", "").replace(",", "").strip())

    # ===================== CONVERT PRICE =====================
    try:
        CurrentPrice = float(CleanPrice)
    except ValueError:
        print(Fore.RED +"❌ Failed To Convert Price")
        continue

    # ===================== SHOW PRODUCT =====================
    print(Fore.CYAN + "\n" + "-" * 65)
    print(Style.BRIGHT +Fore.GREEN +f"📦 Product:\n{ProductTitle}")
    print(Fore.YELLOW +f"\n💰 Current Price: {PriceText}")
    print(Fore.MAGENTA +f"🎯 Target Price: ₹{TargetPrice}")
    print(Fore.CYAN + "-" * 65)

    # ===================== PRICE CHECK =====================
    if CurrentPrice <= TargetPrice:
        print(Style.BRIGHT +Fore.GREEN +"\n🎉 Product Is Within Your Budget!")

        # ===================== EMAIL MESSAGE =====================
        Message = f"""\nSubject: Amazon Price Alert! 🎉 \n
        Good News!\n
        Your product is now within your target price.\n
        📦 Product: {ProductTitle}\n
        💰 Current Price: {PriceText}\n
        🔗 Product URL:{ProductURL}\n
                    """

        # ===================== SEND EMAIL =====================
        try:
            Connection = smtplib.SMTP("smtp.gmail.com",587)
            Connection.starttls()
            Connection.login(
                UserGmail,
                UserPassword
                )

            Connection.sendmail(
                                from_addr=UserGmail,
                                to_addrs=ReceiverMail,
                                msg=Message.encode("utf-8")
                                )

            Connection.close()
            print(Fore.GREEN +"📧 Email Alert Sent Successfully!")

        except Exception as error:
            print(Fore.RED +f"❌ Email Failed: {error}")
    else:
        Difference = CurrentPrice - TargetPrice
        print(Style.BRIGHT +Fore.RED +f"\n❌ Still Expensive By ₹{Difference:.2f}")

    # ===================== CONTINUE / EXIT =====================
    while True:
        Ask = input(Fore.CYAN +"\nDo You Want To Check Another Product?\n"
                               "👉 Type 'C' or 'Continue'\n""👉 Type 'E' or 'Exit'\n\n").lower()

        # ===================== EXIT =====================
        if Ask in ["e", "exit"]:
            print(Fore.YELLOW +"\n⏳ Exiting Application...")
            time.sleep(2)
            print(Style.BRIGHT +Fore.GREEN +"🙏 Thank You For Using Amazon Price Tracker")
            Replay = False
            break

        # ===================== CONTINUE =====================
        elif Ask in ["c", "continue"]:
            print(Fore.GREEN +"\n🔄 Restarting Application...\n")
            time.sleep(1)
            break

        # ===================== INVALID =====================
        else:
            print(Fore.RED +"\n❌ Invalid Input! Try Again.")

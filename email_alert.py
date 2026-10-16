import smtplib


def BuildAlertMessage(ProductTitle, PriceText, ProductURL):
    return f"""\nSubject: Amazon Price Alert! 🎉 \n
        Good News!\n
        Your product is now within your target price.\n
        📦 Product: {ProductTitle}\n
        💰 Current Price: {PriceText}\n
        🔗 Product URL:{ProductURL}\n
                    """


def SendPriceAlert(SettingsData, ProductTitle, PriceText, ProductURL):
    Message = BuildAlertMessage(ProductTitle, PriceText, ProductURL)

    Connection = smtplib.SMTP("smtp.gmail.com", 587)
    Connection.starttls()
    Connection.login(SettingsData["UserGmail"], SettingsData["UserPassword"])

    Connection.sendmail(
        from_addr=SettingsData["UserGmail"],
        to_addrs=SettingsData["ReceiverMail"],
        msg=Message.encode("utf-8"),
    )

    Connection.close()

import requests
from bs4 import BeautifulSoup
from config import Headers


class BaseScraper:
    """Base class every platform scraper extends."""

    Name = "Generic"
    DomainKeywords = []

    def Matches(self, ProductURL):
        return any(Keyword in ProductURL for Keyword in self.DomainKeywords)

    def Fetch(self, ProductURL):
        Response = requests.get(ProductURL, headers=Headers)
        Soup = BeautifulSoup(Response.text, "html.parser")
        return Response, Soup

    # ===================== OFFICIAL-SELLER MARKERS =====================
    # Seller names that mean "fulfilled/sold by the platform itself",
    # treated as official even if they don't match the brand name.
    PlatformOwnedSellerHints = []

    def ExtractTitleText(self, Soup):
        raise NotImplementedError

    def ExtractPriceText(self, Soup):
        raise NotImplementedError

    def ExtractSellerText(self, Soup):
        """Override per-platform. Returns None when seller info can't be found."""
        return None

    def CleanPrice(self, PriceText):
        return (
            PriceText.replace("₹", "")
            .replace("Rs.", "")
            .replace(",", "")
            .strip()
        )

    def GetProductDetails(self, ProductURL):
        Response, Soup = self.Fetch(ProductURL)

        TitleText = self.ExtractTitleText(Soup)
        PriceText = self.ExtractPriceText(Soup)

        if not TitleText or not PriceText:
            return None

        ProductTitle = TitleText.strip()
        CleanPriceValue = self.CleanPrice(PriceText.strip())

        try:
            CurrentPrice = float(CleanPriceValue)
        except ValueError:
            return None

        SellerText = self.ExtractSellerText(Soup)
        SellerText = SellerText.strip() if SellerText else None

        return {
            "Title": ProductTitle,
            "PriceText": PriceText.strip(),
            "Price": CurrentPrice,
            "StatusCode": Response.status_code,
            "Seller": SellerText,
            "Platform": self.Name,
            "Authenticity": self.CheckAuthenticity(ProductURL, ProductTitle, SellerText),
        }

    def CheckAuthenticity(self, ProductURL, ProductTitle, SellerText):
        """Best-effort heuristic, not a legal guarantee of authenticity.
        Flags "likely official" vs "third-party seller" vs "unknown" so the
        user knows to double check instead of assuming a result is certain.
        """
        IsSecure = ProductURL.lower().startswith("https://")

        if not SellerText:
            return {
                "Status": "UNKNOWN",
                "SellerName": "Not Found",
                "Reason": "Seller Information Could Not Be Detected",
                "Secure": IsSecure,
            }

        SellerLower = SellerText.lower()
        BrandGuess = ProductTitle.split()[0].lower() if ProductTitle else ""

        IsPlatformOwned = any(
            Hint.lower() in SellerLower for Hint in self.PlatformOwnedSellerHints
        )
        IsBrandMatch = bool(BrandGuess) and BrandGuess in SellerLower

        if IsPlatformOwned or IsBrandMatch:
            return {
                "Status": "OFFICIAL",
                "SellerName": SellerText,
                "Reason": (
                    f"Sold By {self.Name}" if IsPlatformOwned else "Sold By Brand-Matching Seller"
                ),
                "Secure": IsSecure,
            }

        return {
            "Status": "THIRD_PARTY",
            "SellerName": SellerText,
            "Reason": "Sold By A Third-Party Seller, Not The Brand/Platform Itself",
            "Secure": IsSecure,
        }

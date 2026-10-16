from .base import BaseScraper


class MyntraScraper(BaseScraper):
    Name = "Myntra"
    DomainKeywords = ["myntra.com"]
    PlatformOwnedSellerHints = ["myntra"]

    def ExtractTitleText(self, Soup):
        BrandElement = Soup.select_one("h1.pdp-title")
        NameElement = Soup.select_one("h1.pdp-name")

        if BrandElement and NameElement:
            return f"{BrandElement.get_text()} {NameElement.get_text()}"

        return NameElement.get_text() if NameElement else None

    def ExtractPriceText(self, Soup):
        PriceElement = Soup.select_one("span.pdp-price strong, span.pdp-price")
        return PriceElement.get_text() if PriceElement else None

    def ExtractSellerText(self, Soup):
        SellerElement = Soup.select_one("div.supplier-sellerName, span.supplier-sellerName")
        return SellerElement.get_text() if SellerElement else None

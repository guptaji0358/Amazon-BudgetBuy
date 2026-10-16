from .base import BaseScraper


class FlipkartScraper(BaseScraper):
    Name = "Flipkart"
    DomainKeywords = ["flipkart.com"]
    PlatformOwnedSellerHints = ["flipkart", "retailnet", "supercomnet", "wsretail"]

    def ExtractTitleText(self, Soup):
        TitleElement = Soup.select_one("span.VU-ZEz, span.B_NuCI, h1.yhB1nd")
        return TitleElement.get_text() if TitleElement else None

    def ExtractPriceText(self, Soup):
        PriceElement = Soup.select_one("div.Nx9bqj.CxhGGd, div._30jeq3._16Jk6d, div._30jeq3")
        return PriceElement.get_text() if PriceElement else None

    def ExtractSellerText(self, Soup):
        SellerElement = Soup.select_one(
            "#sellerName span, div._1RLviY span, div.yeLuwb"
        )
        return SellerElement.get_text() if SellerElement else None

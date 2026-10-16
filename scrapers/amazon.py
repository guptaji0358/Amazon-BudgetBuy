from .base import BaseScraper


class AmazonScraper(BaseScraper):
    Name = "Amazon"
    DomainKeywords = ["amazon.in", "amazon.com", "amzn.to", "amazon."]
    PlatformOwnedSellerHints = ["amazon", "appario", "cloudtail", "rk world"]

    def ExtractTitleText(self, Soup):
        TitleElement = Soup.find(id="productTitle")
        return TitleElement.get_text() if TitleElement else None

    def ExtractPriceText(self, Soup):
        PriceElement = Soup.select_one(".a-price .a-offscreen")
        if not PriceElement:
            PriceElement = Soup.select_one("#priceblock_dealprice, #priceblock_ourprice")
        return PriceElement.get_text() if PriceElement else None

    def ExtractSellerText(self, Soup):
        SellerElement = Soup.select_one(
            "#sellerProfileTriggerId, #merchant-info a, #merchant-info"
        )
        return SellerElement.get_text() if SellerElement else None

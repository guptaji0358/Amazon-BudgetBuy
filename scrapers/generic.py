import re
from .base import BaseScraper

# ===================== CURRENCY PATTERN =====================
PricePattern = re.compile(r"(₹|Rs\.?|INR|\$|USD)\s?[\d,]+(\.\d{1,2})?")

# ===================== COMMON PRICE CSS HINTS =====================
PriceSelectorHints = [
    "[class*='price']",
    "[id*='price']",
    "[itemprop='price']",
    "meta[property='product:price:amount']",
    "meta[property='og:price:amount']",
]

# ===================== COMMON TITLE CSS HINTS =====================
TitleSelectorHints = [
    "meta[property='og:title']",
    "[itemprop='name']",
    "h1",
]

# ===================== COMMON SELLER CSS HINTS =====================
SellerSelectorHints = [
    "[class*='seller']",
    "[id*='seller']",
    "[itemprop='seller']",
    "[class*='sold-by']",
    "[class*='soldBy']",
]


class GenericScraper(BaseScraper):
    """Runtime fallback scraper that works on any e-commerce site
    it hasn't seen before, using heuristics instead of fixed selectors.
    This is what makes the tracker platform-agnostic instead of
    limited to a hardcoded whitelist of sites."""

    Name = "Generic"
    DomainKeywords = []

    def Matches(self, ProductURL):
        return True

    def ExtractTitleText(self, Soup):
        for Selector in TitleSelectorHints:
            Element = Soup.select_one(Selector)
            if not Element:
                continue

            if Element.name == "meta":
                Content = Element.get("content")
                if Content:
                    return Content

            else:
                Text = Element.get_text().strip()
                if Text:
                    return Text

        if Soup.title:
            return Soup.title.get_text()

        return None

    def ExtractPriceText(self, Soup):
        for Selector in PriceSelectorHints:
            for Element in Soup.select(Selector):
                if Element.name == "meta":
                    Content = Element.get("content")
                    if Content and self._LooksLikePrice(Content):
                        return Content
                    continue

                Text = Element.get_text().strip()
                Match = PricePattern.search(Text)
                if Match:
                    return Match.group(0)

        # ===================== WHOLE PAGE FALLBACK =====================
        PageText = Soup.get_text(" ")
        Match = PricePattern.search(PageText)
        return Match.group(0) if Match else None

    def ExtractSellerText(self, Soup):
        for Selector in SellerSelectorHints:
            Element = Soup.select_one(Selector)
            if not Element:
                continue

            Text = Element.get_text().strip()
            if Text and len(Text) < 80:
                return Text

        return None

    def _LooksLikePrice(self, Text):
        return bool(re.search(r"[\d,.]+", Text))

    def CleanPrice(self, PriceText):
        PriceText = super().CleanPrice(PriceText)
        PriceText = re.sub(r"[^\d.]", "", PriceText)
        return PriceText

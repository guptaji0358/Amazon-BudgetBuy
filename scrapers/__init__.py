from .amazon import AmazonScraper
from .flipkart import FlipkartScraper
from .myntra import MyntraScraper
from .generic import GenericScraper

# ===================== KNOWN PLATFORM SCRAPERS =====================
# Each has hand-tuned selectors for higher accuracy on that one site.
KnownScrapers = [
    AmazonScraper(),
    FlipkartScraper(),
    MyntraScraper(),
]

# ===================== RUNTIME FALLBACK =====================
# Catches every platform NOT in the list above, so support isn't
# capped at whatever sites were coded in ahead of time.
FallbackScraper = GenericScraper()


def GetScraperForURL(ProductURL):
    for ScraperInstance in KnownScrapers:
        if ScraperInstance.Matches(ProductURL):
            return ScraperInstance

    # ===================== ANY OTHER SHOPPING SITE =====================
    return FallbackScraper


def SupportedPlatforms():
    KnownNames = [ScraperInstance.Name for ScraperInstance in KnownScrapers]
    return KnownNames + ["Any Other Site (Auto-Detect)"]

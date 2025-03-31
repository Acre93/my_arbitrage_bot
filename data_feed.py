# data_feed.py

import requests

class DataFeed:
    def __init__(self):
        print("DataFeed initialized.")

    def fetch_all_data(self):
        """
        Fetch real BTC price from CoinGecko,
        plus a fake list of DeFi yields, to demonstrate structure.
        """
        print("DataFeed: Fetching data...")

        btc_price = self._fetch_btc_price()
        defi_yields = self._mock_defi_yields()

        data = {
            "prices": {
                "BTC": btc_price
            },
            "yields": defi_yields,
            # We'll keep these empty for now; you can fill them in as you expand:
            "funding_rates": {},
            "bridge_info": {},
            "gas_fees": {}
        }

        return data

    def _fetch_btc_price(self):
        """
        Uses CoinGecko's public API to get BTC's price in USD.
        No API key needed. 
        """
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin",
            "vs_currencies": "usd"
        }
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            btc_price_usd = data["bitcoin"]["usd"]
            print(f"Fetched BTC price in USD: {btc_price_usd}")
            return btc_price_usd
        except Exception as e:
            print(f"Error fetching BTC price: {e}")
            # Fallback price if API fails
            return 28000.0

    def _mock_defi_yields(self):
        """
        A mock list of DeFi yields (just as placeholders).
        In the future, you could fetch from Aave, Compound, or others.
        """
        return [
            {"name": "Aave", "apr": 0.03, "audited": True, "liquidity": 2_000_000},
            {"name": "Compound", "apr": 0.025, "audited": True, "liquidity": 1_500_000},
            {"name": "Curve", "apr": 0.04, "audited": True, "liquidity": 3_000_000},
        ]
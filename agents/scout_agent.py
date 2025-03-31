# agents/scout_agent.py

class ScoutAgent:
    def __init__(self, data_feed):
        self.data_feed = data_feed
        self.memory_cache = {}
        print("ScoutAgent initialized.")

    def discover_opportunities(self):
        print("ScoutAgent: Checking for opportunities...")

        # 1. Fetch the latest data from the data_feed
        all_data = self.data_feed.fetch_all_data()

        # 2. Cache it for other agents if needed
        self.memory_cache['latest_data'] = all_data

        # 3. Create a list to hold discovered opportunities
        opportunities = []

        # Example logic #1: If BTC price is above 25k, consider a "short" or something
        btc_price = all_data["prices"].get("BTC", 0)
        if btc_price > 25000:
            opportunities.append({
                "type": "BTC_short",
                "description": f"BTC price at {btc_price}, possible short opportunity",
                "price": btc_price
            })

        # Example logic #2: If a DeFi yield is above 3%, treat it as an opportunity
        for protocol in all_data["yields"]:
            if protocol["apr"] > 0.03:
                opportunities.append({
                    "type": "DeFi_yield",
                    "protocol": protocol["name"],
                    "apr": protocol["apr"],
                    "liquidity": protocol["liquidity"]
                })

        print(f"ScoutAgent: Found {len(opportunities)} opportunities.")
        return opportunities
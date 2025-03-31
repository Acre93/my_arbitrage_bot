# agents/risk_agent.py

class RiskAgent:
    def __init__(self):
        print("RiskAgent initialized.")

    def evaluate_risk(self, opportunity, market_data):
        """
        Basic logic: assign a 'risk_score' based on liquidity and 
        whether the protocol is audited, etc.
        
        opportunity: dict from ScoutAgent (e.g. {"type": "DeFi_yield", "protocol": "...", "apr": ...})
        market_data: the latest_data fetched by data_feed (with "yields", "prices", etc.)
        """

        risk_score = 0
        risk_reasons = []

        # Only handle DeFi_yield type for now
        if opportunity["type"] == "DeFi_yield":
            protocol_name = opportunity["protocol"]
            # find a matching entry in market_data["yields"]
            protocol_info = next(
                (p for p in market_data["yields"] if p["name"] == protocol_name),
                None
            )
            if protocol_info:
                # 1. Liquidity check
                liquidity = protocol_info["liquidity"]
                if liquidity < 1_000_000:
                    risk_score += 2
                    risk_reasons.append("Low liquidity (< $1M)")

                # 2. Audited check
                if not protocol_info["audited"]:
                    risk_score += 1
                    risk_reasons.append("Protocol not audited")

            else:
                # If we can't find the protocol data, treat it as high risk
                risk_score += 3
                risk_reasons.append("No info about this protocol in market_data")

        elif opportunity["type"] == "BTC_short":
            # Example: shorting BTC might have market volatility risk
            price = opportunity.get("price", 0)
            # If price is high, we consider shorting less risky (?), or you can invert it
            # We'll keep it simple:
            if price > 30000:
                # maybe that's riskier
                risk_score += 2
                risk_reasons.append("BTC price is very high - potential volatility")
            else:
                risk_score += 1
                risk_reasons.append("Shorting always has some risk")

        # Return the aggregated results
        return {
            "risk_score": risk_score,
            "risk_reasons": risk_reasons
        }
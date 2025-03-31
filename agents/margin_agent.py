# agents/margin_agent.py

class MarginAgent:
    def __init__(self):
        print("MarginAgent initialized.")

    def calculate_expected_return(self, opportunity, cost_data, risk_data):
        """
        Returns a dict with "expected_apr" and "risk_penalty".
        
        opportunity: e.g. {"type": "DeFi_yield", "protocol": "...", "apr": ...}
        cost_data: e.g. {"bridge_fee": 0.001, "slippage": 0.001, "gas_fee": 10}
        risk_data: e.g. {"risk_score": 2, "risk_reasons": ["Low liquidity"]}
        """

        # Start with base APR if it's DeFi, or define a placeholder if it's BTC short
        if opportunity["type"] == "DeFi_yield":
            base_apr = opportunity.get("apr", 0.0)
        elif opportunity["type"] == "BTC_short":
            # This might represent some separate logic
            # Let's just say shorting yields some hypothetical 5% 
            base_apr = 0.05
        else:
            base_apr = 0.0

        bridging_fee = cost_data.get("bridge_fee", 0.001)  # 0.1% default
        slippage = cost_data.get("slippage", 0.001)        # 0.1% default
        risk_score = risk_data.get("risk_score", 0)

        # Example penalty: each risk point = 0.5% of yield
        risk_penalty = 0.005 * risk_score

        net_apr = base_apr - bridging_fee - slippage - risk_penalty

        return {
            "expected_apr": net_apr,
            "risk_penalty": risk_penalty
        }
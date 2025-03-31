# board.py

from agents.scout_agent import ScoutAgent
from agents.risk_agent import RiskAgent
from agents.margin_agent import MarginAgent
from agents.execution_agent import ExecutionAgent
from agents.audit_agent import AuditAgent
from data_feed import DataFeed

class Board:
    def __init__(self, wallet_interface=None):
        print("Board (Meta-Agent) initialized.")

        self.data_feed = DataFeed()
        self.scout_agent = ScoutAgent(self.data_feed)
        self.risk_agent = RiskAgent()
        self.margin_agent = MarginAgent()
        self.execution_agent = ExecutionAgent(wallet_interface)
        self.audit_agent = AuditAgent()

    def run_cycle(self, size_btc=0.1):
        # 1. Scout
        opportunities = self.scout_agent.discover_opportunities()

        if not opportunities:
            print("No opportunities found.")
            return None

        # 2. Evaluate with Risk & Margin
        top_opp = opportunities[0]  # just pick the first one for now
        market_data = self.data_feed.fetch_all_data()
        risk_data = self.risk_agent.evaluate_risk(top_opp, market_data)
        margin_data = self.margin_agent.calculate_expected_return(
            top_opp, 
            cost_data={"bridge_fee": 0.001, "slippage": 0.001, "gas_fee": 10}, 
            risk_data=risk_data
        )

        # 3. Execute trade
        result = self.execution_agent.execute_trade(top_opp, size_btc)
        # 4. Audit
        self.audit_agent.log_trade({
            "opportunity": top_opp,
            "risk_data": risk_data,
            "margin_data": margin_data,
            "execution_result": result
        })

        return result
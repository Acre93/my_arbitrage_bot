# agents/audit_agent.py

class AuditAgent:
    def __init__(self, log_path="trades_log.json"):
        self.log_path = log_path
        print("AuditAgent initialized.")

    def log_trade(self, trade_details):
        print(f"AuditAgent: Logging trade details: {trade_details}")
        # In future, write to a file or DB
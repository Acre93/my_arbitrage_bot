# agents/execution_agent.py

class ExecutionAgent:
    def __init__(self, wallet_interface):
        self.wallet = wallet_interface
        print("ExecutionAgent initialized.")

    def execute_trade(self, opportunity, size_btc: float):
        print(f"ExecutionAgent: Executing trade for {opportunity} with size {size_btc} BTC...")

        # Example bridging logic if it's a DeFi yield opportunity
        if opportunity["type"] == "DeFi_yield":
            # 1. Wrap or bridge BTC
            bridge_tx = self.wallet.wrap_btc(size_btc)

            # 2. Deposit or stake
            tx_trade = self.wallet.execute_defi_trade(
                protocol=opportunity["protocol"],
                amount=size_btc,
                action="deposit"
            )
            return {"bridge_tx": bridge_tx, "trade_tx": tx_trade}

        elif opportunity["type"] == "BTC_short":
            # Maybe you do a different flow for shorting
            # For demonstration, let's skip bridging
            tx_trade = self.wallet.execute_defi_trade(
                protocol="some_derivatives_platform",
                amount=size_btc,
                action="open_short"
            )
            return {"bridge_tx": None, "trade_tx": tx_trade}

        else:
            print("Unknown opportunity type, no action taken.")
            return {"bridge_tx": None, "trade_tx": None}
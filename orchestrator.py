# orchestrator.py
from board import Board
from wallet_interface import PaperTradingWallet, RealWallet

def main():
    # 1. Decide if we want paper or real trading
    paper_trading = True  # or False

    # 2. Create the appropriate wallet
    if paper_trading:
        wallet_interface = PaperTradingWallet(initial_balance_btc=1.0)
    else:
        wallet_interface = RealWallet(private_key="FAKE_PRIVATE_KEY")

    # 3. Pass it to the board
    meta_agent_board = Board(wallet_interface=wallet_interface)
    meta_agent_board.run_cycle(size_btc=0.01)

if __name__ == "__main__":
    main()
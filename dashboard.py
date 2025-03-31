# dashboard.py
import streamlit as st
import os
import csv

from wallet_interface import PaperTradingWallet
# If you need to access your Board or DataFeed, import them too

def main():
    st.title("BTC AI Arbitrage Monitor")

    # Example: Show current paper BTC balance
    if "paper_wallet" not in st.session_state:
        # Initialize a session wallet in paper mode for demonstration
        st.session_state.paper_wallet = PaperTradingWallet(initial_balance_btc=1.0, trades_csv="paper_trades.csv")
    
    paper_wallet = st.session_state.paper_wallet
    st.subheader("Paper Trading Wallet Balance")
    st.write(f"{paper_wallet.get_balance()} BTC")

    st.subheader("Recent Paper Trades (from CSV)")
    if os.path.exists("paper_trades.csv"):
        with open("paper_trades.csv", "r") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if rows:
                for row in reversed(rows[-5:]):  # show last 5
                    st.write(f"**Time**: {row['timestamp']} | **Action**: {row['action']} | "
                             f"**Protocol**: {row['protocol']} | **Amount**: {row['amount_btc']} BTC | "
                             f"**Balance After**: {row['balance_btc_after']} BTC | "
                             f"**PNL**: {row['pnl_usd']} USD")
            else:
                st.write("No trades logged yet.")
    else:
        st.write("paper_trades.csv not found.")

    # Example: If you want to display discovered opportunities
    # you'd run your Board or ScoutAgent here, or load from logs.
    # st.subheader("Opportunities")
    # ... more code if you want

if __name__ == "__main__":
    main()
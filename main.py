import os
import time
import random
from datetime import datetime

USE_TESTNET = os.getenv("USE_TESTNET", "True") == "True"
SIMULER = os.getenv("SIMULER", "True") == "True"

symbol = "DOGEUSDT"
quantity = 100
price = round(random.uniform(0.1, 0.2), 5)

def simulate_trade(side, symbol, quantity, price):
    print(f"{datetime.now()} | SIMULERT {side} {quantity} {symbol} @ {price}")

def main():
    print("Starter tradingbot...")
    if SIMULER:
        print("🚨 KJØRER I SIMULERT MODUS – INGEN EKTE HANDLER 🚨")
    else:
        print("🔴 ADVARSEL: PRØVER Å HANDLE MED EKTE API")

    while True:
        now = datetime.now()
        print(f"{now} | Breakout signal: Kjøper @ {price}")
        if SIMULER:
            simulate_trade("BUY", symbol, quantity, price)
        else:
            print("Her ville en ekte ordre blitt plassert.")
        time.sleep(60)

if __name__ == "__main__":
    main()

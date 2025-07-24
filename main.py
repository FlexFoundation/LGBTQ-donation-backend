from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse, RedirectResponse
import datetime

app = FastAPI()

# === Crypto Wallets ===
BTC_WALLET = "bc1qh8es4m9mjua5w08qv00"
USDT_WALLET = "TE6bcewMeHxn8USQ65baJh4ynx8Qw5dvop"

# === Sample Logs (in-memory only) ===
donation_logs = []

@app.get("/")
def root():
    return {
        "message": "Welcome to the LGBTQ+ Donation API",
        "donate_card": "/donate/card",
        "donate_btc": f"Send BTC to: {BTC_WALLET}",
        "donate_usdt": f"Send USDT (TRC20) to: {USDT_WALLET}",
        "logs": "/logs"
    }

@app.post("/donate/card")
def donate_with_card(name: str = Form(...), amount: float = Form(...)):
    # Simulated Flutterwave logic (mock)
    donation = {
        "name": name,
        "amount": amount,
        "method": "Card (Flutterwave)",
        "time": datetime.datetime.now().isoformat()
    }
    donation_logs.append(donation)
    return RedirectResponse(url="/thank-you", status_code=302)

@app.get("/donate/btc")
def donate_btc():
    return {"wallet": BTC_WALLET}

@app.get("/donate/usdt")
def donate_usdt():
    return {"wallet": USDT_WALLET}

@app.get("/logs")
def view_logs():
    return donation_logs

@app.get("/thank-you")
def thank_you():
    return {"message": "Thank you for your donation and support ❤️"}

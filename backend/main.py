from fastapi import FastAPI
from datetime import date

app = FastAPI(title="Murex Practice Platform", version="0.1.0")

trades = [
    {"id":"FX-10482","product":"EUR/USD Forward","counterparty":"Global Bank","notional":"€5.0M","status":"BOOKED","pnl":24350},
    {"id":"IRS-7721","product":"Interest Rate Swap","counterparty":"Capital Markets","notional":"$25M","status":"CONFIRMED","pnl":81240},
    {"id":"FX-10479","product":"FX Spot","counterparty":"Market Counterparty","notional":"$2.5M","status":"PENDING","pnl":-3820},
]

@app.get("/api/health")
def health():
    return {"status":"UP","service":"murex-backend","date":date.today().isoformat()}

@app.get("/api/trades")
def get_trades():
    return {"count":len(trades),"trades":trades}

@app.get("/api/market-data")
def market_data():
    return {"quotes":[
        {"instrument":"EUR/USD","value":1.1652,"change":0.24},
        {"instrument":"USD/INR","value":88.42,"change":-0.08},
        {"instrument":"USD/JPY","value":147.82,"change":0.11},
        {"instrument":"EUR/INR","value":103.08,"change":0.15}
    ]}

from fastapi import APIRouter, Query
import requests

router = APIRouter()

@router.get("/kline")
def get_kline(
    symbol: str = Query("AMD", description="股票代码，如AMD"),
    interval: str = Query("1min", description="K线周期，如1min/5min/15min/30min/60min/4h/1d")
):
    """
    获取指定股票的K线数据
    """
    # 请将下面的url替换为你的行情API服务实际地址
    url = "http://103.106.191.243:8000/kline"
    params = {"symbol": symbol, "interval": interval}
    resp = requests.get(url, params=params)
    return resp.json() 
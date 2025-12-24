import os
import tushare as ts
import pandas as pd

ts.set_token(os.getenv("TUSHARE_TOKEN"))
pro = ts.pro_api()


print("API Success")

TS_CODE = '000555.SZ'

df = pro.daily(
    ts_code=TS_CODE,
    start_date='20240101',
    end_date='20241231',
    adj='qfq'
)

'''stocks = pro.stock_basic(
    exchange='',
    list_status='L',
    fields='ts_code,symbol,name,area,industry,list_date'
)
'''

df = df.sort_values("trade_date")

df.to_csv("../data/test")

print(df.head())
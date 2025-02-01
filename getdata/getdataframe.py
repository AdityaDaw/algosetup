import time
import pandas as pd
from pandas import DataFrame

from sessioncreator import apiSessionCreator



def get_time(time_string):
    data = time.strptime(time_string, '%d-%m-%Y %H:%M:%S')
    return time.mktime(data)

def get_time_series_data(start:str,end:str,exchange='NSE',token='26000',interval = 60,columns = ['time','into','inth','intl','intc']):
    """'17-06-2024 00:00:00'"""
    start_timestamp = get_time(start)
    end_timestamp = get_time(end)
    api = apiSessionCreator()
    # holdings = api.get_holdings()
    # if holdings is None:
    #   print("The holding details is empty")
    # else:
    #     print(holdings)
    ret = api.get_time_price_series(exchange=exchange,starttime=start_timestamp,endtime=end_timestamp,interval=interval,token=token)
    if ret is None:
        raise RuntimeError("The return data is None")
    df : DataFrame = pd.DataFrame.from_dict(ret)[columns]
    df.index = df['time']
    df = df.rename(columns={'intc':'Close','inth':'High','intl':'Low','into':'Open'}).drop(['time'],axis=1)
    df["Open"] = df["Open"].astype(float)
    df["Close"] = df["Close"].astype(float)
    df["High"] = df["High"].astype(float)
    df["Low"] = df["Low"].astype(float)
    df = df.sort_index(ascending=True)
    df["change"] = df["Open"].pct_change() * 100
    return df


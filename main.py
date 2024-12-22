import timeit

import numpy as np
import pandas as pd

from Procedure.main import Procedure
from algorithm import signal, ohlc_plot_candles_main, signal_chart, performance
from algorithm.indicators import ma,smoothed_ma
from getdata.getdataframe import get_time, get_time_series_data
import matplotlib.pyplot as plt
from algorithm.indicators import *

if __name__ == '__main__':
    mysql = Procedure()
    start_secs = '17-06-2024 00:00:00'
    end_secs = '17-08-2024 00:00:00'
    ret = get_time_series_data(start_secs,end_secs,interval=5)
    my_data = ret.values.astype('f')
    my_data = on_neck_signal(my_data)
    org_data = pd.DataFrame(my_data)
    ohlc_plot_candles_main(my_data)
    print(my_data)
    my_data = org_data.loc[org_data[5] == -1]
    print(my_data)
    my_data = org_data.loc[org_data[4] == 1]
    print(my_data)
    print(ret)

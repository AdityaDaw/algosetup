import timeit

from algorithm import signal, ohlc_plot_candles, signal_chart, performance
from algorithm.indicators import ma,smoothed_ma
from getdata.getdataframe import get_time, get_time_series_data
import matplotlib.pyplot as plt



if __name__ == '__main__':
    start_secs = '01-06-2024 00:00:00'
    end_secs = '26-06-2024 00:00:00'
    ret = get_time_series_data(start_secs,end_secs)

    my_data = ret.values
    my_data = ma(my_data, 20, 3, 4)
    print(my_data)
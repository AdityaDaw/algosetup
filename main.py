import dataclasses
import json
import multiprocessing

import pandas as pd

from Procedure.orchestration import orchestration
from getdata.getdataframe import get_time_series_data
from reading_symbol.get_symbol import get_stocks

if __name__ == '__main__':
    # start_secs = '01-02-2025 00:00:00'
    # end_secs = '01-02-2025 11:24:00'
    # df = get_time_series_data(start_secs,end_secs,interval=60)
    # my_data = ret.values.astype('f')
    # print(my_data)
    # print(df)


    # print(get_stocks())

    list_returned = orchestration()

    with open("stock_data.json", "w") as f:
        json.dump([dataclasses.asdict(d) for d in list_returned], f, indent=4)
        print("Data written to stock_data.json")

    # num_cores = multiprocessing.cpu_count()
    # print(f"Number of available CPU cores: {num_cores}")


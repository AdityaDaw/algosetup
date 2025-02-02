import dataclasses
import json
import multiprocessing

import pandas as pd

from Procedure.filtering_stock import stock_filtered_list
from Procedure.market_order_orchestration.batch_creation import batch_creation
from getdata.getdataframe import get_time_series_data
from reading_symbol.data_class import STOCK
from reading_symbol.get_symbol import get_stocks

if __name__ == '__main__':
    # start_secs = '01-02-2025 00:00:00'
    # end_secs = '01-02-2025 11:24:00'
    # df = get_time_series_data(start_secs,end_secs,interval=60)
    # my_data = ret.values.astype('f')
    # print(my_data)
    # print(df)


    # print(get_stocks())

    # list_returned = stock_filtered_list()
    #
    # with open("stock_data.json", "w") as f:
    #     json.dump([dataclasses.asdict(d) for d in list_returned], f, indent=4)
    #     print("Data written to stock_data.json")

    with open("stock_data.json", "r") as f:
        loaded_data = json.load(f)

    # Convert JSON back to Data Classes
    loaded_objects = [STOCK(**d) for d in loaded_data]

    print("Data loaded from file:", loaded_objects)

    batch_creation(loaded_objects)



import dataclasses
import json
import multiprocessing
from datetime import datetime

import pandas as pd

from Procedure.filtering_stock import stock_filtered_list
from Procedure.market_order_orchestration.final_update_orchestration import final_update_batch_creation
from Procedure.market_order_orchestration.initial_insert_batch_creation import batch_creation
from getdata.getdataframe import get_time_series_data
from reading_symbol.data_class import STOCK
from reading_symbol.get_symbol import get_stocks, logger
from util.logger import CustomLogger

logger = CustomLogger.create_logger(__name__)

def main_function():
    now = datetime.now()

    at_2_55_pm = now.replace(hour=14, minute=55, second=0, microsecond=0)
    at_3_15_pm = now.replace(hour=15, minute=15, second=0, microsecond=0)

    number_of_day = datetime.today().weekday()

    logger.info(f"Today is {number_of_day}")

    while True:
        if number_of_day not in [5,6]:
            logger.info(f"Today is not Sunday or Saturday going with the loop")

            if datetime.now() == at_2_55_pm:
                logger.info("Starting the loop at 2:55 pm")
                list_returned = stock_filtered_list()

                with open("stock_data.json", "w") as f:
                    json.dump([dataclasses.asdict(d) for d in list_returned], f, indent=4)
                    print("Data written to stock_data.json")
                with open("stock_data.json", "r") as f:
                    loaded_data = json.load(f)

                # Convert JSON back to Data Classes
                loaded_objects = [STOCK(**d) for d in loaded_data]

                print("Data loaded from file:", loaded_objects)
                batch_id = batch_creation(loaded_objects)

            if datetime.now() == at_3_15_pm:
                final_update_batch_creation(batch_id)

        else:
            logger.warning(f"Today is Sunday or Saturday - {number_of_day}")
            logger.warning(f"Breaking from loop")
            break





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
    #
    # with open("stock_data.json", "r") as f:
    #     loaded_data = json.load(f)
    #
    # # Convert JSON back to Data Classes
    # loaded_objects = [STOCK(**d) for d in loaded_data]
    # #
    # print("Data loaded from file:", loaded_objects)
    # #
    # batch_id = batch_creation(loaded_objects)
    #
    # final_update_batch_creation(batch_id)

    main_function()



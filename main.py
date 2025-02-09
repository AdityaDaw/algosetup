import dataclasses
import json
import multiprocessing
from datetime import datetime
from time import sleep

import pandas as pd

from Procedure.filtering_stock import stock_filtered_list
from Procedure.market_order_orchestration.final_update_orchestration import final_update_batch_creation
from Procedure.market_order_orchestration.initial_insert_batch_creation import batch_creation
from getdata.getdataframe import get_time_series_data
from reading_symbol.data_class import STOCK
from reading_symbol.get_symbol import get_stocks, logger
from util.logger import CustomLogger
from datetime import time

logger = CustomLogger.create_logger(__name__)


def main_function():
    now = datetime.now()

    at_3_15_pm = time(15, 15, 0)
    at_3_30_pm = time(15, 30, 0)

    number_of_day = datetime.today().weekday()

    logger.info(f"Today is {number_of_day}")

    while True:
        if number_of_day not in [5, 6]:
            # logger.debug(f"Today is not Sunday or Saturday going with the loop")

            if datetime.now() == at_3_15_pm:
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

            if datetime.now() == at_3_30_pm:
                final_update_batch_creation(batch_id)

        else:
            logger.warning(f"Today is Sunday or Saturday - {number_of_day}")
            logger.warning(f"Breaking from loop")
            break

def first_slot() -> int:
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

    return batch_id

def second_slot(batch_id: int):
    final_update_batch_creation(batch_id)

def main_orchestrator():
    number_of_day = datetime.today().weekday()
    logger.info(f"Today is {number_of_day}")
    if number_of_day not in [5, 6]:
        logger.info("Today is not a sunday or Saturday")

        current_first_time = datetime.now()
        target_first_time = current_first_time.replace(hour=14, minute=55, second=0, microsecond=0)
        target_second_time = current_first_time.replace(hour=15, minute=15, second=0, microsecond=0)

        first_delay = (target_first_time - current_first_time).total_seconds()
        if first_delay > 0:
            logger.info(f"Waiting {first_delay} seconds...")
            sleep(first_delay)
            logger.info(f"In Current time {datetime.now()}")
            batch_id = first_slot()
        else:
            logger.info("Target time has already passed.")

        current_second_time = datetime.now()
        second_delay = (target_second_time - current_second_time).total_seconds()
        if second_delay > 0:
            logger.info(f"Waiting {second_delay} seconds...")
            sleep(second_delay)
            logger.info(f"In Current time {datetime.now()}")
            second_slot(batch_id)
        else:
            logger.info("Target time has already passed.")




if __name__ == '__main__':

    main_orchestrator()


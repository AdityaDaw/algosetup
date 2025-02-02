import csv
import dataclasses
import multiprocessing
import os.path

from typing import List

from sqlalchemy.orm import sessionmaker

from gettoken.additionalfunction import createengine
from reading_symbol.data_class import STOCK
from util.logger import CustomLogger
from util.tables.stocks import Stocks

logger = CustomLogger.create_logger(__name__)

def get_stocks() -> List[STOCK]:
    stocks : List[STOCK] = []
    stock_file_name = os.path.join(os.path.abspath(os.path.dirname(__file__)), "NSE_symbols.txt")

    with open(stock_file_name, 'r') as file:
    # Use csv.reader to handle commas and spaces
        reader = csv.reader(file, skipinitialspace=True)
        for row in reader:
            # Ensure the row has exactly 3 fields
            if len(row) == 8:
                Exchange,Token,LotSize,Symbol,TradingSymbol,Instrument,TickSize, _ = row
                # Convert age to integer and create Person instance
                try:
                    stock = STOCK(Exchange,Token,int(LotSize),Symbol,TradingSymbol,Instrument,float(TickSize))
                    stocks.append(stock)
                except ValueError:
                    print(f"Skipping invalid row: {row}")
    return stocks


def insert_stocks():
    list_of_stocks = get_stocks()
    logger.info(f"We have got the list as - {list_of_stocks}")
    with multiprocessing.Pool(processes=5) as pool:  # Use 4 CPU cores
        results = pool.map(process_orchestration, list_of_stocks)
    filtered_data = [item for item in results if item is not None]


def process_orchestration(stock: STOCK):
    try:
        logger.info(f"We are trying to insert the data in Batches table for ")
        engine  =  createengine()
        Session = sessionmaker(bind=engine)
        session = Session()
        new_entry = Stocks(**dataclasses.asdict(stock))
        session.add(new_entry)
        session.commit()
        last_insert_id = new_entry.TRADING_SYMBOL
        logger.info(f"Last Inserted entry id is - {last_insert_id}")
        session.close()
        return last_insert_id
    except Exception as ex:
        logger.exception(f"Error while inserting data in the table {str(ex)}")




if __name__ == "__main__":
    insert_stocks()
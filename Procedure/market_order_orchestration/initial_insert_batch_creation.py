import multiprocessing
from datetime import datetime, timedelta
from symbol import return_stmt
from typing import List, Optional, Tuple

from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from algorithm.simple_logic import check_change_is_greater, get_last_traded_price
from getdata import get_time_series_data
from gettoken.additionalfunction import createengine, gettoday
from reading_symbol.data_class import STOCK
from util.logger import CustomLogger
from util.tables.batches import Batches

logger =  CustomLogger.create_logger(__name__)

def batch_creation(list_of_stocks :List[STOCK]):
    logger.info(f"We have got the list as - {list_of_stocks}")
    batch_id = get_batch_id()
    logger.info(f"Batch Id is - {batch_id}")
    mapped_with_batch_id = [(batch_id,stock) for stock in list_of_stocks]
    with multiprocessing.Pool(processes=10) as pool:  # Use 4 CPU cores
        results = pool.map(process_orchestration, mapped_with_batch_id)
    filtered_data = [item for item in results if item is not None]

    return batch_id


def insert_data(batch_id: int, stock :STOCK, selling_price: float, quantity : int) -> int:
    try:
        logger.info(f"We are trying to insert the data in Batches table for ")
        engine  =  createengine()
        Session = sessionmaker(bind=engine)
        session = Session()
        new_entry = Batches(
            BATCH_ID = batch_id,
            DATE = str(gettoday()),
            TRADING_SYMBOL = stock.TRADING_SYMBOL,
            TRADING_TOKEN = stock.TOKEN,
            STATUS = "Open",
            SELLING_PRICE = selling_price,
            QUANTITY = quantity,
            VALUE = quantity * selling_price
        )
        session.add(new_entry)
        session.commit()  # Save changes
        last_insert_id = new_entry.ID
        logger.info(f"Last Inserted entry id is - {last_insert_id}")
        return last_insert_id
    except Exception as ex:
        logger.exception(f"Error while inserting data in the table {str(ex)}")

def get_batch_id() -> int:
    try:
        engine  =  createengine()
        today = str(gettoday())
        query = f"select IFNULL( max(BATCH_ID),0) last_batch_id from FlatTrade.Batches"
        conn = engine.connect()
        logger.debug("Data Base connection opened")
        result = conn.execute(text(query))
        conn.close()
        logger.debug("Data Base connection closed")
        engine.dispose()
        logger.debug("Engine has been disposed")
        res = result.all()
        for result in res:
            return int(result.last_batch_id) + 1
    except Exception as ex:
        logger.exception("There is some issue while getting the batch ID from data base")
        raise ex

def process_orchestration(batch_id_mapped_stock: Tuple[int,STOCK]) -> Optional[STOCK]:
    try:
        batch_id, stock = batch_id_mapped_stock
        logger.info(f"Running for - {stock.TRADING_SYMBOL}")
        sell_price = get_sell_price(stock)
        logger.info(f"Last Traded price for the stock - {stock.TRADING_SYMBOL} is {sell_price}")
        fixed_price = 5000
        quantity = int(fixed_price / sell_price)
        logger.info(f"Batch id is {batch_id}")
        last_insert_id = insert_data(
            batch_id,stock,sell_price,quantity
        )
        logger.info(f"Last insert id after successful insert is - {last_insert_id}")

        purchase_price = get_buy_price(stock)
        logger.info(f"We are going o purchase the stock in this price - {purchase_price}")

        return last_insert_id

    except RuntimeError as rt:
        logger.exception(f"There is error while running this {stock.TRADING_SYMBOL}")
        logger.error(str(rt))

    return None


def get_sell_price(stock: STOCK) -> float:
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    prior_time = (datetime.now() - timedelta(minutes=25)).strftime('%d-%m-%Y %H:%M:%S')
    start_secs = '01-02-2025 14:00:00'
    end_secs = '01-02-2025 15:00:00'

    df = get_time_series_data(prior_time, now, interval=1, token=stock.TOKEN,exchange=stock.EXCHANGE)
    print(df)
    last_price = get_last_traded_price(df)
    return last_price


def get_buy_price(stock: STOCK)-> float:
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    prior_time = (datetime.now() - timedelta(minutes=25)).strftime('%d-%m-%Y %H:%M:%S')
    start_secs = '01-02-2025 15:00:00'
    end_secs = '01-02-2025 15:15:00'

    df = get_time_series_data(prior_time, now, interval=1, token=stock.TOKEN,exchange=stock.EXCHANGE)
    print(df)
    last_price = get_last_traded_price(df)
    return last_price

if __name__ == '__main__':
    now = datetime.now()
    today931 = now.replace(hour=15, minute=00, second=0, microsecond=0).strftime('%d-%m-%Y %H:%M:%S')
    today315 = now.replace(hour=15, minute=20, second=0, microsecond=0).strftime('%d-%m-%Y %H:%M:%S')

    print(str(today315))

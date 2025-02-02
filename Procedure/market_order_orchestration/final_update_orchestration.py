import multiprocessing
from typing import List

from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker

from Procedure.market_order_orchestration.initial_insert_batch_creation import get_buy_price
from gettoken.additionalfunction import createengine
from reading_symbol.data_class import dataclass_from_dict, BATCH, STOCK
from util.logger import CustomLogger
from util.tables.batches import Batches
from util.tables.stocks import Stocks

logger = CustomLogger.create_logger(__name__)

def final_update_batch_creation(batch_id : int):
    logger.info(f"Running for the batch id - {batch_id}")
    batches_list = get_list_batches(batch_id)
    with multiprocessing.Pool(processes=10) as pool:  # Use 4 CPU cores
        results = pool.map(update_orchestration, batches_list)
        filtered_data = [item for item in results if item is not None]


def get_list_batches(batch_id : int) ->  List[BATCH]:
    # Create Engine and Session
    engine = createengine()
    Session = sessionmaker(bind=engine)
    session = Session()

    # Select and update specific rows
    open_list = session.query(Batches).filter(and_(Batches.BATCH_ID == batch_id,Batches.STATUS == "Open")).all()

    list_of_stock_dataclass = [dataclass_from_dict(BATCH,stock.__dict__) for stock in open_list]

    logger.info(f"Batches data {list_of_stock_dataclass}")

    session.close()
    return list_of_stock_dataclass


def update_orchestration(batch : BATCH):
    try:
        logger.info(f"Running for {batch}")
        stock = get_particular_stock(batch.TRADING_TOKEN)
        final_buy_price = get_buy_price(stock)

        # Create Engine and Session
        engine = createengine()
        Session = sessionmaker(bind=engine)
        session = Session()

        # Select and update specific rows
        stock = session.query(Batches).filter(Batches.ID == batch.ID).update({"PURCHASE_PRICE": final_buy_price})

        # Commit changes
        session.commit()
        logger.debug(f"Purchase price updated successfully for - {batch.TRADING_SYMBOL}")
        session.close()


    except Exception as ex:
        logger.exception(f"Error while running for this {batch}")


def get_particular_stock(token_id : str) -> STOCK:
    try:
        # Create Engine and Session
        engine = createengine()
        Session = sessionmaker(bind=engine)
        session = Session()

        # Select and update specific rows
        stock = session.query(Stocks).filter(Stocks.TOKEN == token_id).first()
        stock_objet = dataclass_from_dict(STOCK,stock.__dict__)
        session.close()
        logger.info(f"Got stock object as {stock_objet}")
        return stock_objet
    except Exception as ex:
        logger.exception("Error while getting the particular stock")

import multiprocessing
from typing import List, Optional

from pandas import DataFrame

from algorithm.simple_logic import check_change_is_greater
from getdata import get_time_series_data
from reading_symbol.data_class import STOCK
from reading_symbol.get_symbol import get_stocks


def orchestration() -> List[STOCK]:
    list_of_stocks: List[STOCK] = get_stocks()
    filtered_stock: List[STOCK] = []
    with multiprocessing.Pool(processes=10) as pool:  # Use 4 CPU cores
        results = pool.map(process_orchestration, list_of_stocks)
    filtered_data = [item for item in results if item is not None]
    return filtered_data

def process_orchestration(stock: STOCK) -> Optional[STOCK]:
    try:
        print(f"Running for - {stock.TRADING_SYMBOL}")
        start_secs = '01-02-2025 00:00:00'
        end_secs = '01-02-2025 11:24:00'
        if stock.INSTRUMENT in ["INDEX","EQ"]:
            df = get_time_series_data(start_secs, end_secs, interval=60, token=stock.TOKEN,exchange=stock.EXCHANGE)
            if check_change_is_greater(df):
                print(stock.TRADING_SYMBOL)
                return stock
    except RuntimeError as rt:
        print(f"There is error while running this {stock.TRADING_SYMBOL}")
        print(str(rt))

    return None

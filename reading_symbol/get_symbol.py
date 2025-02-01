import csv
import os.path

from typing import List

from reading_symbol.data_class import STOCK


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

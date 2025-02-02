from dataclasses import dataclass, replace, fields
from datetime import datetime
from typing import Optional


@dataclass
class STOCK:
    # Exchange,Token,LotSize,Symbol,TradingSymbol,Instrument,TickSize,
    EXCHANGE:str
    TOKEN: str
    LOT_SIZE: int
    SYMBOL: str
    TRADING_SYMBOL : str
    INSTRUMENT :str
    TICK_SIZE : float

@dataclass
class BATCH:
    ID : int
    BATCH_ID: int
    DATE : datetime
    TRADING_SYMBOL: str
    TRADING_TOKEN: Optional[str]
    STATUS: Optional[str]
    PURCHASE_PRICE: Optional[float]
    SELLING_PRICE: Optional[float]
    QUANTITY: int
    VALUE: Optional[float]

# Generic function to convert dictionary to dataclass
def dataclass_from_dict(data_class, data_dict):
    """Convert a dictionary to a dataclass instance."""
    field_names = {f.name for f in fields(data_class)}
    filtered_data = {k: v for k, v in data_dict.items() if k in field_names}
    return data_class(**filtered_data)

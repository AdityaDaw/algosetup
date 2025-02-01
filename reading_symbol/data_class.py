from dataclasses import dataclass

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

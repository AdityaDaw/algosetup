from typing import Optional

from sqlalchemy.orm import mapped_column, Mapped

from util.tables.batches import Base


class Stocks(Base):
    __tablename__ = "Stocks"
    TOKEN: Mapped[str] = mapped_column(primary_key=True)
    EXCHANGE: Mapped[str]
    LOT_SIZE: Mapped[Optional[str]]
    SYMBOL: Mapped[Optional[str]]
    TRADING_SYMBOL: Mapped[Optional[str]]
    INSTRUMENT: Mapped[Optional[str]]
    TICK_SIZE: Mapped[float]

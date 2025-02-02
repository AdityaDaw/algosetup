from datetime import datetime
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql.functions import now


class Base(DeclarativeBase):
    pass

class Batches(Base):
    __tablename__ = "Batches"
    ID: Mapped[int] = mapped_column(primary_key=True)
    BATCH_ID: Mapped[int]
    DATE: Mapped[Optional[datetime]] = mapped_column(insert_default=now())
    TRADING_SYMBOL: Mapped[Optional[str]]
    TRADING_TOKEN: Mapped[Optional[str]]
    STATUS: Mapped[Optional[str]]
    PURCHASE_PRICE: Mapped[Optional[float]]
    SELLING_PRICE: Mapped[Optional[float]]
    QUANTITY: Mapped[int]
    VALUE: Mapped[Optional[float]]

    def __repr__(self):
        return f"ID - {self.ID}"


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from squirrel.db.tables.table_base import TableBase


class TableTicks(TableBase):
    __tablename__ = 'ticks'

    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer,  ForeignKey('stocks.id'))
    date = Column(Integer, index=True)
    open = Column(Float, index=True)
    high = Column(Float, index=True)
    low = Column(Float, index=True)
    close = Column(Float, index=True)
    volume = Column(Integer, index=True)

    def __init__(self, stock_id, date, open, high, low, close, volume):
        self.stock_id = stock_id
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __repr__(self):
        return ("<{}("
                "stock_id={stock_id!r}, "
                "date={date!r}, "
                "open={open!r}, "
                "high={high!r}, "
                "low={low!r}, "
                "close={close!r}, "
                "volume={volume!r}"
                ")>".format(type(self).__name__,
                            stock_id=self.stock_id,
                            date=self.date,
                            open=self.open,
                            high=self.high,
                            low=self.low,
                            close=self.close,
                            volume=self.volume,
                            ))

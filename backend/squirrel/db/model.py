# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


import logging
import sqlalchemy as sa

from squirrel.db.tables.base.table_base import Base

from squirrel.db.tables import ALL_TABLES


log = logging.getLogger(__name__)


class Model(object):

    def __init__(self, dburl=None, verbose=False):
        if dburl is None:
            dburl = 'sqlite://'  # in memory DB
        self._engine = sa.create_engine(dburl,
                                        echo=verbose,
                                        pool_reset_on_return=None)
        self.metadata = Base.metadata
        self.registeredTableClass = []

        for table in ALL_TABLES:
            # Force consumption of the tables class name
            self.registerTable(table)

    def start(self, create=True):
        self.metadata.bind = self._engine

        Session = sa.orm.sessionmaker()
        Session.configure(bind=self._engine)
        self._session = Session()
        if create:
            log.debug("Creating all tables...")
            self.metadata.create_all(self._engine)

    def stop(self):
        self._session.close()

    @property
    def session(self):
        return self._session

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, tb):
        self.stop()

    def registerTable(self, tableClassName):
        self.registeredTableClass.append(tableClassName)

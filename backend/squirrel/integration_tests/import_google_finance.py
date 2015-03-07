from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from twisted.internet import defer

from squirrel.common.unittest import TestCase
from squirrel.dam.google_finance import GoogleFinance

# Uncomment this to true to debug unclean reactor
# from twisted.internet.base import DelayedCall
# DelayedCall.debug = True


log = logging.getLogger(__name__)


class IntegrationTest(TestCase):

    @defer.inlineCallbacks
    def test_GoodTicker_DataIsNotEmpty(self):
        log.debug("requesting google finance AAPL")
        res = yield GoogleFinance().getTicks(ticker="AAPL",
                                             exchange="NASDAQ",
                                             intervalMin=60 * 24,
                                             nbIntervals=2)
        self.assertNotEmpty(res)
        for tick in res[:10]:
            self.assertNotEqual(tick.open, 0)
            self.assertNotEqual(tick.volume, 0)
        [log.debug("{!r}".format(r)) for r in res[:10]]

    @defer.inlineCallbacks
    def test_BadTicker_ExceptionOccurs(self):
        yield self.assertInlineCallbacksRaises(Exception,
                                               GoogleFinance().getTicks,
                                               ticker="BAD_TICKER",
                                               exchange="NASDAQ",
                                               intervalMin=60 * 24,
                                               nbIntervals=2)

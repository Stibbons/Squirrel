from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import calendar
import datetime
import time

from textwrap import dedent as textwrap_dedent

__all__ = ['dedent']


def dedent(text):
    return textwrap_dedent(text).lstrip()


def getTodayEpoch():
    return calendar.timegm(time.gmtime())


def dateTimeToEpoch(da):
    return calendar.timegm(da.timetuple())


def epochTimeStringToDatatime(epochString):
    return datetime.datetime.fromtimestamp(int(epochString))


def string2EpochTime(stingTime, format='%Y-%m-%d'):
    ''' convert string time to epoch time '''
    return int(time.mktime(datetime.datetime.strptime(stingTime, format).timetuple()))


def string2datetime(stringTime, format='%Y-%m-%d'):
    ''' convert string time to epoch time'''
    return datetime.datetime.strptime(stringTime, format)
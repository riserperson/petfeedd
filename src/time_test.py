import time
import queue
import datetime
import logging

import petfeedd

from worker import Worker
from models.Feed import Feed
from models.FeedEvent import FeedEvent


time_query0 = '19:35:00'
time_query1 = '19:35'
print(Feed.select().where((Feed.time==time_query0) | (Feed.time==time_query1)).count())

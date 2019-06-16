from pushbullet import Pushbullet
from datetime import datetime
import queue
import logging
import time

import petfeedd

from worker import Worker
from models.Feed import Feed
from models.FeedEvent import FeedEvent

pb = Pushbullet('o.4rL9QTU3iKQFOoDxobG6q5ZuJZsr4lkL')
pushes = pb.get_pushes()

for item in pushes:
    if 'target_device_iden' in item.keys():
        if item['target_device_iden'] == 'ujyphE0lqwesjEmye7u6sS':
            if item['body'] == 'feed':
                print('foo')

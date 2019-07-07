from pushbullet import Pushbullet
from datetime import datetime as dt, timedelta
import queue
import logging
import time

import petfeedd

from worker import Worker
from models.Feed import Feed
from models.FeedEvent import FeedEvent

class PushWorker(Worker):
    def __init__(self, feed_queue, *args, **kwargs):
        self.feed_queue = feed_queue
        super().__init__(*args, **kwargs)

    def run(self):
        logging.getLogger('petfeedd').info('Starting push worker.')
        while True:
            if self.stopped():
                logging.getLogger('petfeeed').info('Stopping the time worker.')
                return
            pb = Pushbullet('o.4rL9QTU3iKQFOoDxobG6q5ZuJZsr4lkL')
            pushes = pb.get_pushes()
            bc_feed_pushes = [ ]
            for item in pushes:
                if 'target_device_iden' in item.keys():
                    if item['target_device_iden'] == 'ujyphE0lqwesjEmye7u6sS':
                        if item['body'] == 'feed':
                            bc_feed_pushes.append(item)

            for bc_feed_push in bc_feed_pushes:
                push_time = dt.fromtimestamp(bc_feed_push['created'])
                if time.time() - push_time.timestamp() < 3600:
                    if FeedEvent.select().where(FeedEvent.date_updated > dt.now() - timedelta(hours=1)).count() == 0:
                        logging.getLogger('petfeedd').info('Found pushbullet feed request.')
                        feed_event = FeedEvent.create(size=1, name='PushBullet', weight=0)
                        self.feed_queue.put(feed_event)
            logging.getLogger('petfeedd').info('Push worker resetting at: ' + dt.now().strftime('%d/%m/%Y %H:%M'))
            time.sleep(3600)

from peewee import *

from models.BaseModel import BaseModel

class FeedEvent(BaseModel):
    name = CharField()
    size = IntegerField(default=0)
    weight = IntegerField(default=0)

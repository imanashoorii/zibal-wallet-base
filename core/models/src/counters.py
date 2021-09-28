from mongoengine import *
import mongoengine_goodjson as gj


class Counters(gj.Document):

    id = StringField()
    sequence_value = IntField(default=0, min_value=0)

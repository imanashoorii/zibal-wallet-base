from mongoengine import *
import mongoengine_goodjson as gj
import datetime


class Wallet(gj.Document):

    walletId = IntField(required=True)
    balance = IntField(default=0)
    name = StringField()
    withdrawableBalance = IntField(default=0)
    createdAt = DateTimeField(default=datetime.datetime.now)
    updatedAt = DateTimeField()

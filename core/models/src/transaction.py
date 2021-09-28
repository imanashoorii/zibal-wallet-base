from mongoengine import *
import mongoengine_goodjson as gj
import datetime
from core.service.utils import toJalaliDateTime


class Transaction(gj.Document):

    walletId = IntField(required=True)
    transactionId = IntField(required=True)
    trackId = IntField()
    amount = IntField()
    walletCredit = IntField()
    status = IntField(default=0)
    createdAt = DateTimeField(default=datetime.datetime.now)

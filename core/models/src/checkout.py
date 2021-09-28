from mongoengine import *
import mongoengine_goodjson as gj
import datetime


class CheckoutQueue(gj.Document):
    checkoutId = IntField(required=True, min_value=1)
    walletId = IntField(required=True)
    amount = IntField()
    iban = StringField()
    checkoutDelay = IntField(default=1)
    createdAt = DateTimeField(default=datetime.datetime.now)

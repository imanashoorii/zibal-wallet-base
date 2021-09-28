# Models
import datetime

from core.models.src.checkout import CheckoutQueue
from core.models.src.transaction import Transaction
from core.models.src.wallet import Wallet

# Utils
from core.service.utils import jsonResponse, toJalaliDateTime
from core.service.incrementalId import getNextSequenceValue
from pymongo import MongoClient, WriteConcern
import requests


def db():
    client = MongoClient("mongodb://root:root@localhost:27017/admin")
    wc_majority = WriteConcern("majority", wtimeout=1000)
    database = client.get_database('zibal_db', write_concern=wc_majority)
    session = client.start_session()
    return database, session


database, session = db()


def createWallet(name):
    if name:
        new_wallet = Wallet(
            name=name,
            walletId=getNextSequenceValue('walletId'),
        )
        withdraw = new_wallet.balance - 80000
        new_wallet.withdrawableBalance = withdraw

        if new_wallet.save():
            data = {
                "message": 'موفق',
                "result": 1,
                "data":
                    {
                        'balance': new_wallet.balance,
                        'withdrawableBalance': withdraw,
                        'name': new_wallet.name,
                        'id': new_wallet.walletId,
                        'createdAt': toJalaliDateTime(new_wallet.createdAt),
                    }
            }

            return jsonResponse(data)
        else:
            pass
    else:
        return jsonResponse(data={'msg': 'name is required'}, status=400)


def walletList():
    all_wallets = []

    for items in Wallet.objects():
        dict = {}
        dict['name'] = items.name
        dict['balance'] = items.balance
        dict['withdrawableBalance'] = items.withdrawableBalance
        dict['id'] = items.walletId

        all_wallets.append(dict)

    data = {
        'message': 'موفق',
        'result': 1,
        'data': all_wallets
    }

    return jsonResponse(data=data)


def checkout(amount, wallet_id, iban, checkout_delay=1):
    if amount and wallet_id and iban is not None:

        wallet = Wallet.objects(walletId=wallet_id)
        if wallet:
            wallet = wallet.get(walletId=wallet_id)
            if wallet.balance >= int(amount):
                new_checkout = CheckoutQueue(
                    checkoutId=getNextSequenceValue('checkoutId'),
                    walletId=wallet_id,
                    amount=amount,
                    iban=iban,
                    checkoutDelay=checkout_delay
                )
                new_checkout.save()

                Wallet.objects(walletId=wallet_id).update(dec__balance=new_checkout.amount)
                data = {
                    "message": 'موفق',
                    "result": 1,
                    "data": {
                        'createdAt': toJalaliDateTime(new_checkout.createdAt),
                        'amount': new_checkout.amount,
                        'id': new_checkout.checkoutId,
                        'iban': new_checkout.iban,
                    }
                }

                return jsonResponse(data)
            else:
                return jsonResponse({'error': 'Insufficient balance!!'}, status=402)
        else:
            return jsonResponse(data={'error': f'Wallet with id {wallet_id} DoesNotExists'}, status=404)
    else:
        return jsonResponse(data={'error': 'field missing'}, status=400)


def charge(amount, walletId):
    wallet = Wallet.objects(walletId=walletId)
    if wallet:
        wallet = wallet.get(walletId=walletId)
        zibal_api = 'https://gateway.zibal.ir/v1/request/'  # -> POST

        req = requests.post(zibal_api, json={"merchant": "zibal", "amount": int(amount),
                                             "callbackUrl": "http://localhost:8000/v1/wallet/charge/verify"}
                            )
        response = req.json()
        track_id = response['trackId']

        new_transaction = Transaction(
            transactionId=getNextSequenceValue('transactionId'),
            walletId=walletId,
            amount=amount,
            trackId=track_id,
            walletCredit=wallet.balance
        )

        new_transaction.save()
        data = {
            'status': new_transaction.status,
            "transactionId": new_transaction.transactionId,
            "id": new_transaction.walletId,
            'amount': new_transaction.amount,
            'walletCredit': new_transaction.walletCredit,
            'trackId': new_transaction.trackId,
            'chargeUrl': f'https://gateway.zibal.ir/start/{track_id}',
            'createdAt': toJalaliDateTime(new_transaction.createdAt)
        }

        return jsonResponse(data=data)
    else:
        return jsonResponse(data={'error': f'Wallet with id {walletId} DoesNotExists'}, status=400)


def verifyAndRecharge(success, track_id):
    zibal_verify_api = 'https://gateway.zibal.ir/v1/verify'

    if int(success) == 1:
        ver = requests.post(zibal_verify_api, json={"merchant": "zibal", "trackId": track_id})
        verify_response = ver.json()

        if not verify_response['result'] == 100:
            return jsonResponse(
                data={'message': verify_response['message'], 'result': verify_response['result']})
        else:
            print(verify_response['message'], verify_response['result'])
            Transaction.objects(trackId=track_id).update(set__status=1)
            transaction = Transaction.objects.get(trackId=track_id)
            Wallet.objects.get(walletId=transaction.walletId).update(inc__balance=transaction.amount,
                                                                     set__updatedAt=datetime.datetime.now)
            wallet = Wallet.objects.get(walletId=transaction.walletId)

            data = {
                'walletId': wallet.walletId,
                'new_balance': wallet.balance,
                'trackId': transaction.trackId,
                'charge_value': transaction.amount,
                'status': transaction.status,
            }

            return jsonResponse(data=data)
    else:
        return jsonResponse(data={'msg': 'recharge is not successful'}, status=400)


def cancelCheckout(checkout_id):
    checkout = CheckoutQueue.objects.get(checkoutId=checkout_id)
    if checkout:
        Wallet.objects.get(walletId=checkout.walletId).update(inc__balance=checkout.amount)
        checkout.delete()
        data = {
            'message': 'موفق',
            'result': 1
        }
        return jsonResponse(data)
    else:
        data = {
            'message': 'مشکلی در لغو تسویه وجود دارد'
        }
        return jsonResponse(data, status=400)


def report():
    all_checkouts = []

    for items in CheckoutQueue.objects():
        dict = {}
        dict['checkoutId'] = items.checkoutId
        dict['walletId'] = items.walletId
        dict['amount'] = items.amount
        dict['iban'] = items.iban
        dict['checkoutDelay'] = items.checkoutDelay
        dict['createdAt'] = toJalaliDateTime(items.createdAt)

        all_checkouts.append(dict)

    return jsonResponse(data=all_checkouts)


def checkoutFilter(checkout_id, iban, amount):
    filters = {}
    if checkout_id:
        filters['checkoutId__in'] = checkout_id
    if amount:
        filters['amount__exact'] = amount
    if iban:
        filters['iban__icontains'] = iban

    checkouts = CheckoutQueue.objects.filter(**filters)

    all_checkouts = []

    for items in checkouts:
        dict = {}
        dict['checkoutId'] = items.checkoutId
        dict['walletId'] = items.walletId
        dict['amount'] = items.amount
        dict['iban'] = items.iban
        dict['checkoutDelay'] = items.checkoutDelay
        dict['createdAt'] = toJalaliDateTime(items.createdAt)

        all_checkouts.append(dict)

    return jsonResponse(data=all_checkouts)


def transactionsFilter(track_id, amount, status):
    filters = {}

    if track_id:
        filters['trackId__icontains'] = track_id
    if amount:
        filters['amount__exact'] = amount
    if status:
        filters['status__icontains'] = status


    transaction = Transaction.objects.filter(**filters)

    all_transaction = []

    for items in transaction:
        dict = {}
        dict['walletId'] = items.walletId
        dict['trackId'] = items.trackId
        dict['amount'] = items.amount
        dict['status'] = items.status

        all_transaction.append(dict)

    return jsonResponse(data=all_transaction)

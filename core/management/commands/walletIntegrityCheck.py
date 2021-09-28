from django.core.management.base import BaseCommand
from core.models.src.transaction import Transaction
from itertools import tee, islice, chain


def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None))
    return zip(prevs, items, nexts)


class Command(BaseCommand):
    help = 'Check Wallet Balance Integrity'

    def add_arguments(self, parser):
        parser.add_argument('-i', '--walletId', type=str, help='walletId integrity check!')

    def handle(self, *args, **kwargs):

        id = kwargs['walletId']

        transactions = Transaction.objects(walletId=id, status=1)
        for pre, item, next in previous_and_next(list(transactions)):
            total = item.amount + item.walletCredit
            if total == next.walletCredit:
                print('Ok!', f"Total is now {total} and next walletCredit is {next.walletCredit}")
            else:
                print(f'there is a difference in walletCredit with transactionId {next.transactionId}')




        # pipeline = [
        #     {
        #         "$match": {
        #             "status": 1,
        #             "walletId": 1
        #         }
        #
        #     },
        #     {
        #         "$group": {
        #             "_id": "$walletId",
        #             "total": {"$sum": "$amount"},
        #         }
        #     }
        # ]
        #
        # transPerWalletId = Transaction.objects.aggregate(*pipeline)
        # for items in transPerWalletId:
        #     print(items)
        # wallets = Wallet.objects(walletId=items['_id'])
        # for wallet in wallets:
        #     if wallet.balance == items['total']:
        #         print('OK!', f'walletId: {items["_id"]}',
        #               f'total: {items["total"]}',
        #               f'balance: {wallet.balance}')
        #     else:
        #         print(f'there is some different in wallet with id {wallet.walletId}')

        # self.stdout.write(self.style.SUCCESS('Done!'))

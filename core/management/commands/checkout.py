from django.core.management.base import BaseCommand
from core.models.src.checkout import CheckoutQueue


class Command(BaseCommand):
    help = 'Get checkout Report'

    def handle(self, *args, **kwargs):
        pipeline = [
            {
                "$group": {
                    "_id": "$iban",
                    "total": {"$sum": "$amount"},
                    "details": {
                        "$push": {
                            "checkoutId": "$checkoutId",
                            "amount": "$amount",
                            "walletId": "$walletId"
                        }
                    }
                },
            },
            {'$merge': 'checkoutTotal'}
        ]
        docs = CheckoutQueue.objects.aggregate(*pipeline)
        # for i in docs:
        #     print(i)

        self.stdout.write(self.style.SUCCESS('Done!'))

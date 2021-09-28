# import django_mongoengine_filter
# from core.models.src.checkout import CheckoutQueue
# from core.models.src.transaction import Transaction
#
#
# class CheckoutFilter(django_mongoengine_filter.FilterSet):
#     class Meta:
#         model = CheckoutQueue
#         fields = ["iban", 'walletId', 'checkoutId', 'checkoutDelay', 'amount']
#
#
# class TransactionsFilter(django_mongoengine_filter.FilterSet):
#     walletId = django_mongoengine_filter.MultipleChoiceFilter()
#
#     class Meta:
#         model = Transaction
#         fields = ['walletId', 'trackId', 'amount', 'status']

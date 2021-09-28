from django.views.decorators.http import require_http_methods
from core.service.wallet_services import report, checkoutFilter, transactionsFilter


@require_http_methods(['GET'])
def checkout_report(request):
    return report()


@require_http_methods(['GET'])
def filter_checkouts(request):
    checkout_id = request.GET.getlist('checkoutId', None)
    iban = request.GET.get('iban', None)
    amount = request.GET.get('amount', None)
    return checkoutFilter(checkout_id, iban, amount)


@require_http_methods(['GET'])
def filter_transactions(request):
    track_id = request.GET.getlist('trackId', None)
    amount = request.GET.get('amount', None)
    status = request.GET.get('status', None)
    return transactionsFilter(track_id, amount, status)

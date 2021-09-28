# Modules
from django.views.decorators.http import require_http_methods

# Utils
from core.service.wallet_services import (createWallet,
                                          walletList,
                                          checkout,
                                          charge,
                                          verifyAndRecharge,
                                          cancelCheckout,
                                          )


@require_http_methods(['POST'])
def wallet_create(request):
    name = request.POST.get('name')
    return createWallet(name)


@require_http_methods(['GET'])
def wallet_list(request):
    return walletList()


@require_http_methods(['POST'])
def wallet_charge(request):
    walletId = request.POST.get('id')
    amount = request.POST.get('amount')
    return charge(amount, walletId)


@require_http_methods(['GET'])
def verify_and_recharge(request):
    success = request.GET.get('success')
    track_id = request.GET.get('trackId')
    return verifyAndRecharge(success, track_id)


@require_http_methods(['POST'])
def wallet_checkout(request):
    amount = request.POST.get('amount')
    wallet_id = request.POST.get('id')
    iban = request.POST.get('iban')
    checkout_delay = request.POST.get('checkoutDelay')

    return checkout(amount, wallet_id, iban, checkout_delay)


@require_http_methods(["POST"])
def cancel_checkout(request):
    checkout_id = request.POST.get('checkoutId')
    return cancelCheckout(checkout_id)

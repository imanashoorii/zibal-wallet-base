from django.conf.urls import url
from core.webservice.wallet import (wallet_create,
                                    wallet_list,
                                    wallet_charge,
                                    wallet_checkout,
                                    verify_and_recharge,
                                    cancel_checkout,
                                    )

urlpatterns = [
    url(r'^wallet/create/$', wallet_create),
    url(r'^wallet/list/$', wallet_list),
    url(r'^wallet/charge/?$', wallet_charge),
    url(r'^wallet/charge/verify$', verify_and_recharge),
    url(r'^wallet/checkout/$', wallet_checkout),
    url(r'^wallet/checkout/cancel/$', cancel_checkout),
]

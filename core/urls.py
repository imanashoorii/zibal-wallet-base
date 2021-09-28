from django.conf.urls import url, include
from core.frontend.wallet import checkout_report, filter_checkouts, filter_transactions

urlpatterns = [
    url('v1/', include('core.webservice.urls')),
    url(r'^api/wallet/checkout-list/$', checkout_report),
    url(r'^api/wallet/transactions/filter/?$', filter_transactions),
    url(r'^api/wallet/checkout/filter/?$', filter_checkouts),
]

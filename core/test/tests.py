from django.test import TestCase


class TestWallet(TestCase):
    """Show setup and teardown"""

    def setUp(self):
        pass

    def test_create_wallet(self):
        """Test Wallet Creation"""

        data = {"name": "test1"}
        response = self.client.post('/v1/wallet/create/', data=data)
        self.assertEqual(response.status_code, 200)

    def test_create_wallet_without_name(self):
        """Test Wallet Creation without name"""

        data_2 = {}
        response = self.client.post('/v1/wallet/create/', data=data_2)
        self.assertEqual(response.status_code, 400)

    def test_charge_wallet(self):
        """Test Charge wallet"""

        data = {'id': 5, 'amount': 40000}
        response = self.client.post('/v1/wallet/charge/', data=data)
        self.assertEqual(response.status_code, 200)

        data_3 = {'amount': 40000}
        response = self.client.post('/v1/wallet/charge/', data=data_3)
        self.assertEqual(response.status_code, 400)

    def test_wallet_checkout(self):
        """Test wallet checkout"""
        data = {
            "id": 3,
            "amount": "85000",
            "iban": 'testest',
            "checkoutDelay": '-1'
        }
        response = self.client.post('/v1/wallet/checkout', data=data)
        self.assertEqual(response.status_code, 200)
        data_2 = {
            "amount": "85000",
            "iban": 'testest',
            "checkoutDelay": '-1'
        }
        response = self.client.post('/v1/wallet/checkout', data=data_2)
        self.assertEqual(response.status_code, 400)
        data_3 = {
            "iban": 'testest',
            "checkoutDelay": '-1'
        }
        response = self.client.post('/v1/wallet/checkout', data=data_3)
        self.assertEqual(response.status_code, 400)
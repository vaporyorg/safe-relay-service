from django.test import TestCase

from eth_account import Account
from hexbytes import HexBytes

from ..models import SafeContract, SafeFunding


class TestModels(TestCase):
    def test_hex_field(self):
        safe_address = Account.create().address
        safe = SafeContract.objects.create(address=safe_address)
        safe_funding = SafeFunding.objects.create(safe=safe)
        safe_funding.deployer_funded_tx_hash = HexBytes('0xabcd')
        safe_funding.save()
        safe_funding.refresh_from_db()
        self.assertEqual(safe_funding.deployer_funded_tx_hash, '0xabcd')

        safe_funding.deployer_funded_tx_hash = bytes.fromhex('abcd')
        safe_funding.save()
        safe_funding.refresh_from_db()
        self.assertEqual(safe_funding.deployer_funded_tx_hash, '0xabcd')

        safe_funding.deployer_funded_tx_hash = '0xabcd'
        safe_funding.save()
        safe_funding.refresh_from_db()
        self.assertEqual(safe_funding.deployer_funded_tx_hash, '0xabcd')

        safe_funding.deployer_funded_tx_hash = 'abcd'
        safe_funding.save()
        safe_funding.refresh_from_db()
        self.assertEqual(safe_funding.deployer_funded_tx_hash, '0xabcd')

        safe_funding.deployer_funded_tx_hash = ''
        safe_funding.save()
        safe_funding.refresh_from_db()
        self.assertEqual(safe_funding.deployer_funded_tx_hash, '0x')

        safe_funding.deployer_funded_tx_hash = None
        safe_funding.save()
        safe_funding.refresh_from_db()
        self.assertIsNone(safe_funding.deployer_funded_tx_hash)

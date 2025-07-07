import unittest
from unittest.mock import patch, Mock

from divine_agents.krak_manager import Krak, KrakManager


class TestKrakManager(unittest.TestCase):
    @patch('divine_agents.krak_manager.urllib.request.urlopen')
    @patch('divine_agents.krak_manager.random.random', return_value=0.9)
    def test_distribute_krak(self, mock_random, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = b"ok"
        manager = KrakManager()
        krak = Krak('Test Task', 'emotion')
        manager.add_krak(krak)
        result = manager.distribute_krak()
        self.assertIn('Distributed Krak', result)
        self.assertEqual(krak.status, 'in-progress')

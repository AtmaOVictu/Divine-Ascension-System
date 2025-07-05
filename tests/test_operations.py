import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.operations import RESOperations


class TestRESOperations(unittest.TestCase):
    def setUp(self):
        self.ops = RESOperations()

    def test_get_existing(self):
        self.assertEqual(self.ops.get_binary_value('RES001'), '00000001')

    def test_add_update_delete(self):
        self.ops.add_operation('RES200', '11001000')
        self.assertEqual(self.ops.get_binary_value('RES200'), '11001000')
        self.ops.update_operation('RES200', '11001001')
        self.assertEqual(self.ops.get_binary_value('RES200'), '11001001')
        self.ops.delete_operation('RES200')
        self.assertEqual(
            self.ops.get_binary_value('RES200'),
            'Napaka: Neznana operacija'
        )

    def test_execute_operation(self):
        result = self.ops.execute_operation('RES000')
        self.assertIn('začetnem stanju', result)


if __name__ == '__main__':
    unittest.main()


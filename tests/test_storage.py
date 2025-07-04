import unittest
from divine_agents.storage import ControlledStorage


class TestControlledStorage(unittest.TestCase):
    def test_store_all_confirmed(self):
        store = ControlledStorage()
        data = [1, 2, 3]
        store.store_slowly(data, delay=0, confirm=lambda x: True)
        self.assertEqual(store.data, data)

    def test_store_none_declined(self):
        store = ControlledStorage()
        data = [1, 2, 3]
        store.store_slowly(data, delay=0, confirm=lambda x: False)
        self.assertEqual(store.data, [])


if __name__ == "__main__":
    unittest.main()

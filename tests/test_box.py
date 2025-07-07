import unittest
from divine_agents.box import BoxWithZero


class TestBoxWithZero(unittest.TestCase):
    def test_initial_state(self):
        box = BoxWithZero('task')
        self.assertEqual(box.data.get('state'), 0)

    def test_update_preserves_zero(self):
        box = BoxWithZero('task', data={'content': 'a'})
        box.update_data({'content': 'b'})
        self.assertEqual(box.data.get('state'), 0)
        self.assertEqual(box.data.get('content'), 'b')

    def test_transition_changes_state(self):
        box = BoxWithZero('task')
        box.transition('processing', {'progress': 50})
        self.assertEqual(box.data['state'], 'processing')
        self.assertEqual(box.data.get('progress'), 50)

    def test_protection(self):
        box = BoxWithZero('task')
        box.set_protection(True)
        with self.assertRaises(PermissionError):
            box.update_data({'x': 1})


if __name__ == '__main__':
    unittest.main()

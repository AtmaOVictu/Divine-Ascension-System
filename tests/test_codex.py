import unittest
from divine_agents.codex import Codex

class TestCodex(unittest.TestCase):
    def test_valid_transition(self):
        c = Codex('initial_state')
        result = c.transition('move')
        self.assertEqual(result, 'State changed to moving_state')
        self.assertEqual(c.state, 'moving_state')
        self.assertEqual(len(c.get_error_log()), 0)

    def test_invalid_command(self):
        c = Codex('initial_state')
        result = c.transition('unknown')
        self.assertTrue(result.startswith('Error'))
        self.assertEqual(len(c.get_error_log()), 1)
        self.assertIn('Invalid Command', c.get_error_log()[0])

if __name__ == '__main__':
    unittest.main()

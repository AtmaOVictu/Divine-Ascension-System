import unittest
from divine_agents import Agent, ConversationManager


class TestConversationManager(unittest.TestCase):
    def test_history_records_lines(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        manager = ConversationManager(a1, a2)
        history = manager.run_conversation(["Kaj je resnica?", "Kaj je pomen?"])
        self.assertEqual(len(history), 2)
        self.assertTrue(all(isinstance(line, str) for line in history))

    def test_dynamic_updates_and_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        manager = ConversationManager(a1, a2)
        for _ in range(8):
            manager.exchange(0, "Test")
        self.assertNotEqual(a1.state, "Ego")
        self.assertGreater(a1.tension, 0.7)


if __name__ == '__main__':
    unittest.main()

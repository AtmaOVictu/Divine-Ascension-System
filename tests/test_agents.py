import unittest
from divine_agents import Agent, Lock, Key, philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_with_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_lock_unlock(self):
        lock = Lock("state_lock", condition="emotion")
        key = Key("emotion_key", key_type="emotion")
        agent = Agent("A")
        agent.add_lock(lock)
        agent.add_key(key)
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertFalse(lock.is_locked())

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("absolutna" in line for line in lines))
        self.assertTrue(any("relativna" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

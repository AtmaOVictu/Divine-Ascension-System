import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.lock import Lock, Key


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_lock_unlock(self):
        agent = Agent("Locked")
        lock = Lock("state lock", condition="emotion")
        agent.add_lock(lock)
        agent.update_emotion(0.9)
        state = agent.transition()
        self.assertEqual(state, "Ego")  # still locked

        key = Key("joy", key_type="emotion")
        agent.add_key(key)
        state = agent.transition()
        self.assertEqual(state, "Jaz")


if __name__ == '__main__':
    unittest.main()

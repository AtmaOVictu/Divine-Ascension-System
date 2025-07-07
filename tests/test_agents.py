import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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

    def test_lock_and_key(self):
        agent = Agent("A")
        lock = Lock("state", condition="emotion")
        key = Key("joy", key_type="emotion")
        agent.add_lock(lock)
        agent.update_emotion(0.8)
        # transition should not occur while locked
        self.assertEqual(agent.transition(), "Ego")
        agent.add_key(key)
        # unlocked, transition now allowed
        self.assertEqual(agent.transition(), "Jaz")


if __name__ == '__main__':
    unittest.main()

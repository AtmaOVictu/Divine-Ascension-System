import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.keylock import Key, Lock


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

    def test_lock_and_key_transition(self):
        agent = Agent("A")
        lock = Lock("L", lock_type="task")
        key = Key("K", key_type="task")
        agent.add_lock(lock)
        agent.add_key(key)
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")


if __name__ == '__main__':
    unittest.main()

import unittest
from divine_agents.agent import Agent
import random
from divine_agents.dialogue import philosophical_dialogue, philosophical_debate


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

    def test_no_transition_below_threshold(self):
        agent = Agent("B")
        agent.update_tension(0.2)
        agent.update_emotion(0.4)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_feel_triggers_transition(self):
        agent = Agent("C")
        agent.feel("strah", 0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_debate(self):
        random.seed(0)
        a1 = Agent("D1")
        a2 = Agent("D2", state="Jaz")
        lines = philosophical_debate(a1, a2, rounds=1)
        self.assertTrue(any("Krog 1" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

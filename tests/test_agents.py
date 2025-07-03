import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, moral_dialogue
from divine_agents.moral_agent import MoralAgent


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


class TestMoralAgent(unittest.TestCase):
    def test_utilitarian_decision(self):
        a1 = MoralAgent("A1", ethics="utilitarianism")
        a2 = MoralAgent("A2")
        a2.update_emotion(1.2)
        a2.update_tension(0.0)
        decision = a1.moral_decision([a2])
        self.assertIn("happiness", decision)

    def test_moral_dialogue(self):
        a1 = MoralAgent("A1")
        a2 = MoralAgent("A2", ethics="deontology")
        lines = moral_dialogue(a1, a2)
        self.assertTrue(any("odlo\u010ditev" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

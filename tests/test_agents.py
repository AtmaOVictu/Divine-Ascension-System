import unittest
from divine_agents.agent import Agent, MultiDimensionalMoralAgent
from divine_agents.dialogue import philosophical_dialogue, moral_dialogue


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

    def test_moral_decision(self):
        agent = MultiDimensionalMoralAgent("A", ethics="virtue")
        decision = agent.moral_decision()
        self.assertIn("virtues", decision)

    def test_moral_dialogue(self):
        a1 = MultiDimensionalMoralAgent("A1", ethics="utilitarianism")
        a2 = MultiDimensionalMoralAgent("A2", ethics="justice")
        lines = moral_dialogue(a1, a2)
        self.assertTrue(any("moral" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

import unittest
from divine_agents.moral_agent import MoralAgent
from divine_agents.moral_dialogue import moral_dialogue


class TestMoralAgent(unittest.TestCase):
    def test_state_transition(self):
        agent = MoralAgent("A")
        agent.update_emotion(0.9)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_decision_utilitarian(self):
        a1 = MoralAgent("A", ethics="utilitarianism", emotion=0.9)
        a2 = MoralAgent("B", ethics="utilitarianism", emotion=0.2)
        decision = a1.make_decision([a2])
        self.assertIn("Maximize", decision)

    def test_moral_dialogue(self):
        a1 = MoralAgent("A")
        a2 = MoralAgent("B", state="Jaz")
        lines = moral_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

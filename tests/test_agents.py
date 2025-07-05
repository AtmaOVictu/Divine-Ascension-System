import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


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

    def test_attributes_update_on_transition(self):
        agent = Agent("A")
        self.assertEqual(agent.norm, "Samooskrba")
        self.assertEqual(agent.shape, "kocka")
        self.assertEqual(agent.moral_value, "Self-preservation")

        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")
        self.assertEqual(agent.norm, "Sodelovanje")
        self.assertEqual(agent.shape, "krogla")
        self.assertEqual(agent.moral_value, "Cooperation")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("norma" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

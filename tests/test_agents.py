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

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        question = "Kakšna je narava resnice?"
        lines = philosophical_dialogue(a1, a2, question=question, emotions=(0.8, 0.6))
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(all(question in line for line in lines[:2]))


if __name__ == '__main__':
    unittest.main()

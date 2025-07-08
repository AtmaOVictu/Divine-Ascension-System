import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        agent.update_emotion(0.9)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost", language="Spanish")
        reply = agent.respond("?Que es la verdad?")
        self.assertIn("verdades", reply)

    def test_dialogue(self):
        a1 = Agent("A1", language="German")
        a2 = Agent("A2", state="Jaz", language="English")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("transitions" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

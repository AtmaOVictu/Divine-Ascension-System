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
        self.assertIn("one", reply)

    def test_language_response(self):
        agent = Agent("B", language="Spanish")
        reply = agent.respond("?")
        self.assertIn("verdad", reply)

    def test_dialogue(self):
        a1 = Agent("A1", language="English")
        a2 = Agent("A2", state="Jaz", language="German")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("transitions" in line for line in lines))

    def test_evolve_transition(self):
        agent = Agent("C", language="German")
        agent.update_emotion(0.6)
        new_state = agent.evolve()
        self.assertEqual(new_state, "Jaz")


if __name__ == '__main__':
    unittest.main()

import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, dynamic_debate


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

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6, "fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_dynamic_debate(self):
        a1 = Agent("X")
        a2 = Agent("Y", state="Jaz")
        lines = dynamic_debate(a1, a2)
        # verify transitions occurred
        self.assertTrue(any("Jaz" in line for line in lines))
        self.assertTrue(any("Enotnost" in line for line in lines))
        # check emotions included in responses
        self.assertTrue(any("anger" in line or "joy" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

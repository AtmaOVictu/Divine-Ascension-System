import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_based_transition(self):
        agent = Agent("B", state="Jaz")
        agent.update_emotion(0.6, "strah")
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_emotional_response_prefix(self):
        agent = Agent("C")
        agent.update_emotion(0.7, "jeza")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("jeza", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        conversation = "\n".join(lines)
        self.assertIn("Enotnost", conversation)
        self.assertIn("jeza", conversation)


if __name__ == '__main__':
    unittest.main()

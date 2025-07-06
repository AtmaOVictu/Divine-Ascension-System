import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.conversation import Conversation


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


class TestConversation(unittest.TestCase):
    def test_emotion_transition(self):
        agent = Agent("B", state="Jaz")
        agent.update_emotion(0.6)
        agent.transition()
        self.assertEqual(agent.state, "Enotnost")

    def test_conversation_run(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        convo = Conversation(a1, a2)
        convo.run([(0.8, 0.0), (0.1, 0.6)])
        self.assertIn("Jaz", a1.history)
        self.assertIn("Enotnost", a2.history)


if __name__ == '__main__':
    unittest.main()

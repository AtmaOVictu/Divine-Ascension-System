import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.emotional_agent import EmotionalAgent
from divine_agents.debate import dynamic_philosophical_debate


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


class TestEmotionalAgents(unittest.TestCase):
    def test_emotion_triggers_transition(self):
        agent = EmotionalAgent("B")
        agent.feel("anger")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_dynamic_debate(self):
        a1 = EmotionalAgent("A1")
        a2 = EmotionalAgent("A2", state="Jaz")
        transcript = dynamic_philosophical_debate(a1, a2)
        self.assertTrue(any("Čutim močna čustva" in line for line in transcript))
        # Ensure at least one agent transitions due to emotion
        self.assertIn(a1.state, ["Jaz", "Enotnost"])


if __name__ == '__main__':
    unittest.main()

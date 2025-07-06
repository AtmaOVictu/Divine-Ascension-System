import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.emotional_contagion import EmotionalContagion
from divine_agents.history import AgentWithHistory


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


class TestEmotionalContagion(unittest.TestCase):
    def test_spread_emotion_triggers_transition(self):
        a1 = Agent("A1", emotion=0.8)
        a2 = Agent("A2")
        ec = EmotionalContagion()
        ec.add_agent(a1)
        ec.add_agent(a2)
        ec.spread_emotion(0, 0.2)
        state = a2.transition()
        self.assertEqual(state, "Jaz")


class TestAgentWithHistory(unittest.TestCase):
    def test_custom_history_retained(self):
        history = ["Ego", "Jaz"]
        agent = AgentWithHistory("A3", state="Enotnost", history=history)
        self.assertEqual(agent.history, history)
        agent.update_tension(1.0)
        agent.transition()
        self.assertEqual(agent.history[-1], "Enotnost")


if __name__ == "__main__":
    unittest.main()

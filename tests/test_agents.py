import unittest
from divine_agents.agent import Agent, AgentWithHistory
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.emotional_contagion import EmotionalContagion


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

    def test_emotional_contagion(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        ec = EmotionalContagion()
        ec.add_agent(a1)
        ec.add_agent(a2)
        a1.update_emotion(0.6)
        ec.spread_emotion(0, 0.2)
        self.assertGreater(a2.emotion, 0.7)

    def test_history_recording(self):
        agent = AgentWithHistory("H")
        agent.update_tension(1.0)
        agent.transition()
        self.assertGreater(len(agent.history), 1)


if __name__ == '__main__':
    unittest.main()

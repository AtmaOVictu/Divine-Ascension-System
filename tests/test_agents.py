import unittest
from divine_agents.agent import Agent
from divine_agents.emotion_cycle import EmotionCycleAgent
from divine_agents.dialogue import philosophical_dialogue, emotional_dialogue


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

    def test_emotion_cycle_agent(self):
        agent = EmotionCycleAgent("EC", frequency=0.5, amplitude=1.5)
        agent.step()
        self.assertIn(agent.state, Agent.STATES)

    def test_emotional_dialogue(self):
        e1 = EmotionCycleAgent("E1")
        e2 = EmotionCycleAgent("E2", state="Jaz")
        lines = emotional_dialogue(e1, e2, steps=5)
        self.assertTrue(len(lines) > 0)


if __name__ == '__main__':
    unittest.main()

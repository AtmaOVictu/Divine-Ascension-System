import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from divine_agents.agent import Agent, CodexAgent
from divine_agents.dialogue import philosophical_dialogue, advanced_philosophical_dialogue


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

    def test_codex_agent_evolve(self):
        agent = CodexAgent("A", emotion_type="positive")
        agent.update_emotion(0.9)
        agent.evolve()
        self.assertEqual(agent.state, "Jaz")

    def test_advanced_dialogue(self):
        a1 = CodexAgent("A1", emotion_type="positive")
        a2 = CodexAgent("A2", state="Jaz", emotion_type="positive")
        lines = advanced_philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

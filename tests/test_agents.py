import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.generator import Generator


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
        gen = Generator(tension_boost=0.8, emotion_boost=0.6)
        lines = philosophical_dialogue(a1, a2, generator=gen)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_generator_triggers_transition(self):
        agent = Agent("G")
        gen = Generator(tension_boost=0.1, emotion_boost=0.6)
        gen.stimulate(agent)
        state = agent.transition()
        self.assertEqual(state, "Jaz")


if __name__ == '__main__':
    unittest.main()

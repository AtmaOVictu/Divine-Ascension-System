import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from divine_agents import (
    Agent,
    ReflectiveAgent,
    MultiAgentSystem,
    philosophical_dialogue,
)


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
        lines = philosophical_dialogue(a1, a2, emotion_pairs=[(0.8, 0.6)])
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_reflective_agent(self):
        agent = ReflectiveAgent("R")
        agent.update_emotion(0.9)
        agent.transition()
        agent.update_emotion(0.9)
        agent.transition()
        agent.update_emotion(0.8)
        agent.transition()
        self.assertTrue(agent.self_reflect())

    def test_multi_agent_system(self):
        system = MultiAgentSystem()
        a1 = Agent("A1")
        a2 = Agent("A2")
        system.add_agent(a1)
        system.add_agent(a2)
        system.update_all_agents(emotions=[0.8, 0.9])
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Jaz")


if __name__ == '__main__':
    unittest.main()

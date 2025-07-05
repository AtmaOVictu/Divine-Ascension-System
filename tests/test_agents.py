import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.system import AgentSystem


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

    def test_intensity(self):
        agent = Agent("B", tension=0.5, emotion=0.4)
        self.assertAlmostEqual(agent.intensity(), 0.2)

    def test_system_density_and_propagation(self):
        agents = [Agent(str(i)) for i in range(3)]
        system = AgentSystem(agents)
        self.assertEqual(system.density(), 3)
        system.propagate()
        self.assertTrue(any(a.state != "Ego" for a in agents))

    def test_average_intensity(self):
        agents = [Agent("A", tension=0.5, emotion=0.4), Agent("B", tension=0.2, emotion=0.2)]
        system = AgentSystem(agents)
        expected = (0.5 * 0.4 + 0.2 * 0.2) / 2
        self.assertAlmostEqual(system.average_intensity(), expected)


if __name__ == '__main__':
    unittest.main()

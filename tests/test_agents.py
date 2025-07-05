import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents import (
    Agent,
    philosophical_dialogue,
    CriticalReflectionAgent,
    LoveHatePhilosophicalAgent,
    CodexSimulation,
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
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_philosophical_context(self):
        agent = LoveHatePhilosophicalAgent("A")
        agent.update_love(0.8)
        agent.update_hate(0.2)
        sim = CodexSimulation([agent])
        sim.run_simulation()
        context = sim.print_agents_philosophical_context()[0]
        self.assertIn("love", context)

    def test_reflection_history(self):
        agent = CriticalReflectionAgent("A")
        agent.update_tension(0.9)
        agent.transition()
        agent.reflect_on_actions()
        self.assertTrue(any("reflecting" in h for h in agent.history))


if __name__ == '__main__':
    unittest.main()

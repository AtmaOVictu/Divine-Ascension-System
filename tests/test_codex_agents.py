import unittest

from divine_agents.codex_agent import (
    LoveHatePhilosophicalAgent,
    CodexSimulation,
)


class TestCodexAgents(unittest.TestCase):
    def test_transition_to_transcendence(self):
        agent = LoveHatePhilosophicalAgent("A", state="Enotnost")
        agent.update_tension(0.9)
        state = agent.transition()
        self.assertEqual(state, "Transcendenca")

    def test_philosophical_analysis_love(self):
        agent = LoveHatePhilosophicalAgent("A")
        agent.update_love(0.8)
        agent.update_hate(0.2)
        agent.philosophical_analysis()
        self.assertIn("love", agent.philosophical_context["A"].lower())

    def test_simulation_run(self):
        agent = LoveHatePhilosophicalAgent("A")
        sim = CodexSimulation([agent])
        lines = sim.run_simulation()
        self.assertTrue(any("Running simulation" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

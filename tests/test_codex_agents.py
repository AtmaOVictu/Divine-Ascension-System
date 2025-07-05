import unittest
from divine_agents.codex import (
    CodexAgent,
    CodexSimulation,
    CriticalReflectionAgent,
    LoveHatePhilosophicalAgent,
)


class TestCodexAgent(unittest.TestCase):
    def test_transition_to_transcendenca(self):
        agent = CodexAgent("A", state="Enotnost")
        agent.update_love(0.9)
        agent.tension = 0.8
        state = agent.transition()
        self.assertEqual(state, "Transcendenca")

    def test_philosophical_context_love(self):
        agent = CodexAgent("A")
        agent.update_love(1.0)
        agent.philosophical_analysis()
        self.assertIn("love", agent.philosophical_context["A"])


class TestCriticalReflectionAgent(unittest.TestCase):
    def test_reflection_history(self):
        agent = CriticalReflectionAgent("B")
        agent.history.append("Jaz")
        agent.reflect_on_actions()
        self.assertTrue(any("reflecting on Jaz" in h for h in agent.history))


class TestLoveHatePhilosophicalAgent(unittest.TestCase):
    def test_evaluate_emotional_impact(self):
        agent = LoveHatePhilosophicalAgent("C")
        agent.update_love(0.7)
        agent.update_hate(0.2)
        agent.evaluate_emotional_impact()
        self.assertTrue(any("motivated by love" in h for h in agent.history))

    def test_simulation(self):
        agent = LoveHatePhilosophicalAgent("Sim")
        sim = CodexSimulation([agent])
        sim.run_simulation()
        self.assertIn(agent.state, CodexAgent.STATES)


if __name__ == "__main__":
    unittest.main()

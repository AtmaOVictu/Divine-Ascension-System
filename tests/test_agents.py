import unittest
from divine_agents.agent import Agent
from divine_agents.codex_agent import (
    CodexAgent,
    CriticalReflectionAgent,
    LoveHatePhilosophicalAgent,
    CodexSimulation,
)
from divine_agents.dialogue import philosophical_dialogue, codex_philosophical_dialogue


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


class TestCodexAgent(unittest.TestCase):
    def test_codex_transition(self):
        agent = CodexAgent("C")
        agent.tension = 0.8
        self.assertEqual(agent.transition(), "Jaz")

    def test_philosophical_analysis(self):
        agent = CodexAgent("C")
        agent.update_love(0.9)
        agent.update_hate(0.1)
        agent.philosophical_analysis()
        self.assertIn("love", agent.philosophical_context["C"].lower())

    def test_reflection(self):
        agent = CriticalReflectionAgent("R")
        agent.history.append("Ego")
        agent.reflect_on_actions()
        self.assertTrue(any("reflecting" in item for item in agent.history))

    def test_emotional_impact(self):
        agent = LoveHatePhilosophicalAgent("L")
        agent.update_love(0.6)
        agent.update_hate(0.2)
        agent.evaluate_emotional_impact()
        self.assertTrue(any("love" in item.lower() for item in agent.history))

    def test_codex_dialogue(self):
        a1 = LoveHatePhilosophicalAgent("A1")
        a2 = LoveHatePhilosophicalAgent("A2", state="Jaz")
        lines = codex_philosophical_dialogue(a1, a2)
        self.assertTrue(any("absolutna" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

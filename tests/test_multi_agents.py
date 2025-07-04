import unittest
from divine_agents.multi_agents import (
    PhilosophicalResearchAgent,
    EmotionalDynamicAgent,
    MoralDilemmaAgent,
    MultiContextualAgentSystem,
)


class TestMultiAgents(unittest.TestCase):
    def test_research_progression(self):
        agent = PhilosophicalResearchAgent("P")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertEqual(agent.research_stage, 1)

    def test_emotional_transition(self):
        agent = EmotionalDynamicAgent("E", emotional_state="Neutral")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertNotEqual(agent.emotional_state, "Neutral")

    def test_moral_dilemma(self):
        agent = MoralDilemmaAgent("M")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertEqual(agent.dilemma, "Selfishness vs. Altruism")

    def test_system_transition_all(self):
        agents = [PhilosophicalResearchAgent("A"), EmotionalDynamicAgent("B")]
        system = MultiContextualAgentSystem(agents)
        lines = system.transition_all()
        self.assertEqual(len(lines), 2)
        self.assertTrue(all("->" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

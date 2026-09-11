import unittest
from divine_agents import (
    Agent,
    AgentWithNumber3,
    AgentWithNumber7,
    PhilosopherAgent,
    HeroAgent,
    agent_dialogue,
)
from divine_agents.dialogue import philosophical_dialogue


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


class TestAdvancedAgents(unittest.TestCase):
    def test_numerology_property(self):
        agent3 = AgentWithNumber3("N3")
        agent7 = AgentWithNumber7("N7")
        self.assertEqual(agent3.numerology_number, 3)
        self.assertEqual(agent7.numerology_number, 7)

    def test_agent_dialogue(self):
        philo = PhilosopherAgent("P")
        hero = HeroAgent("H")
        hero.update_emotion(0.6)
        hero.transition()
        lines = agent_dialogue(philo, hero)
        self.assertTrue(any("meaning" in line for line in lines))
        self.assertTrue(any("justice" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

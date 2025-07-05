import unittest
from divine_agents import (
    Agent,
    ReflectiveAgent,
    philosophical_dialogue,
    MultiAgentSystem,
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

    def test_multi_agent_system(self):
        system = MultiAgentSystem()
        a1 = Agent("A1")
        a2 = Agent("A2")
        system.add_agent(a1)
        system.add_agent(a2)
        # Force predictable transitions
        random_values = [0.9, 0.9]
        for agent, value in zip(system.agents, random_values):
            agent.update_emotion(value)
            agent.transition()
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Jaz")

    def test_reflective_agent(self):
        agent = ReflectiveAgent("A", state="Enotnost")
        agent.update_emotion(0.8)
        agent.transition()
        self.assertTrue(agent.self_reflect())


if __name__ == '__main__':
    unittest.main()

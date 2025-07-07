import unittest

from divine_agents import Agent, MultiDimensionalAgent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_requires_key(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        # Without key the agent should remain in Ego
        self.assertEqual(agent.transition(), "Ego")
        agent.acquire_key("Ego_to_Jaz")
        self.assertEqual(agent.transition(), "Jaz")

    def test_lock_prevents_transition(self):
        agent = Agent("A")
        agent.acquire_key("Ego_to_Jaz")
        agent.add_lock("block")
        agent.update_tension(0.9)
        self.assertEqual(agent.transition(), "Ego")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_multidimensional_agent(self):
        agent = MultiDimensionalAgent("M")
        agent.acquire_key("Ego_to_Jaz")
        agent.update_tension(0.8)
        agent.transition()
        self.assertEqual(agent.dimensions["time"], 1)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

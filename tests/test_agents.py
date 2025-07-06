import unittest

from divine_agents import Agent, philosophical_dialogue, DynamicAgentSystem


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

    def test_dynamic_system(self):
        system = DynamicAgentSystem()
        system.add_agent(Agent("A1"))
        system.add_agent(Agent("A2", state="Jaz"))
        system.add_agent(Agent("A3"))
        lines = system.run_simulation()
        self.assertGreaterEqual(len(lines), 4)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.system import DynamicAgentSystem


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

    def test_system_simulation(self):
        system = DynamicAgentSystem()
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        system.add_agent(a1)
        system.add_agent(a2)
        log = system.run_simulation("Kaj je resnica?", steps=1)
        self.assertEqual(a1.state, "Jaz")
        self.assertGreater(len(log), 0)


if __name__ == '__main__':
    unittest.main()

import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.system import HealthMonitor, DynamicAdjustment


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

    def test_dynamic_adjustment(self):
        agent = Agent("B")
        adjust = DynamicAdjustment()
        msg = adjust.adjust_tension(agent, 0.9)
        self.assertIn("Napetost agenta", msg)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")

    def test_health_monitor(self):
        monitor = HealthMonitor()
        monitor.adjust_health(-60)
        status = monitor.check_system()
        self.assertIn("50", status)


if __name__ == '__main__':
    unittest.main()

import unittest
from divine_agents import Agent, ManagerAgent, SubAgent, philosophical_dialogue


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

    def test_manager_and_logs(self):
        manager = ManagerAgent("M")
        agent = Agent("A")
        helper = SubAgent("S", agent)
        agent.add_sub_agent(helper)
        manager.add_agent(agent)
        agent.update_tension(0.9)
        manager.manage_transitions()
        self.assertEqual(agent.state, "Jaz")
        agent.respond("Kaj je resnica?")
        self.assertTrue(len(helper.logs) > 0)


if __name__ == '__main__':
    unittest.main()

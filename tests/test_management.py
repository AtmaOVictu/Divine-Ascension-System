import unittest

from divine_agents.agent import Agent
from divine_agents.manager import ManagerAgent, SubAgent
from divine_agents.dialogue import managed_philosophical_dialogue


class TestManagerAndSubAgent(unittest.TestCase):
    def test_manager_triggers_transition(self):
        agent = Agent("A1")
        sub = SubAgent("S1", agent)
        agent.add_sub_agent(sub)

        manager = ManagerAgent("M1")
        manager.add_agent(agent)

        agent.update_emotion(0.8)
        manager.manage_transitions()
        agent.respond("Kaj je resnica?")

        self.assertEqual(agent.state, "Jaz")
        self.assertTrue(sub.logs)

    def test_managed_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        manager = ManagerAgent("M1")
        lines = managed_philosophical_dialogue(a1, a2, manager)
        self.assertTrue(any("stanju" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

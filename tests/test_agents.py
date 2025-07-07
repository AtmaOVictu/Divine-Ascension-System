import unittest
from divine_agents import Agent, ManagerAgent, philosophical_dialogue, managed_dialogue


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

    def test_managed_dialogue_logs(self):
        manager = ManagerAgent("M")
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = managed_dialogue(manager, a1, a2)
        # Expect helper logs appended
        self.assertTrue(any("helper-A1" in l for l in lines))
        self.assertTrue(any("helper-A2" in l for l in lines))


if __name__ == "__main__":
    unittest.main()

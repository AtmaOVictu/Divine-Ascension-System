import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_pathos_property(self):
        agent = Agent("B", tension=0.4, emotion=0.6)
        self.assertAlmostEqual(agent.pathos, 0.5)

    def test_sync_pathos_transition(self):
        agent = Agent("C")
        agent.update_tension(0.5)
        agent.update_emotion(0.7)
        agent.sync_pathos()
        self.assertEqual(agent.state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # After the dialogue both agents should have transitioned at least once
        self.assertTrue(a1.state in ("Jaz", "Enotnost"))
        self.assertTrue(any("Resnica" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

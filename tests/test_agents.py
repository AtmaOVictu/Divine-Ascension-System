import unittest

from divine_agents import Agent, OntoState, philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, OntoState.JAZ)

    def test_responses(self):
        agent = Agent("A", state=OntoState.ENOTNOST)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state=OntoState.JAZ)
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("ENOTNOST" in line or "Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

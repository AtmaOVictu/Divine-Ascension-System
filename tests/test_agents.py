import unittest

from divine_agents import Agent, philosophical_dialogue, LogarithmOfReason


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

    def test_logarithm_reason(self):
        agent = Agent("A", tension=0.6, emotion=0.6)
        reason = LogarithmOfReason(agent).calculate()
        self.assertIn("raziskujmo", reason)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))
        self.assertTrue(any("Prehod" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

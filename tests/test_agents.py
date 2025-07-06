import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.contradiction_seeker import NasprotjeIskalec


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


class TestNasprotjeIskalec(unittest.TestCase):
    def test_missing_opposite_triggers_jaz(self):
        seeker = NasprotjeIskalec("Iskalec")
        seeker.find_missing_opposites("empty_space")
        state = seeker.transition()
        self.assertEqual(state, "Jaz")
        self.assertIn("Nasprotje ni prisotno", seeker.missing_opposites)
        self.assertIn("relativna", seeker.respond("Kaj je resnica?"))


if __name__ == '__main__':
    unittest.main()

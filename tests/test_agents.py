import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_ego_to_jaz(self):
        agent = Agent("A")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_jaz_to_enotnost(self):
        agent = Agent("B", state="Jaz")
        agent.update_tension(0.9)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Expect statements about absolute, relative or unified truth
        self.assertTrue(any("absolutna" in l for l in lines))
        self.assertTrue(any("relativna" in l for l in lines))
        self.assertTrue(any("eno" in l for l in lines))


if __name__ == '__main__':
    unittest.main()

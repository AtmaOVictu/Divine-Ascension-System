import unittest
from divine_agents import Agent, ShadowAgent, AngelAgent
from divine_agents.dialogue import philosophical_dialogue


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

    def test_clamping(self):
        agent = Agent("C")
        agent.update_emotion(2.0)
        self.assertLessEqual(agent.emotion, 1)
        agent.update_tension(-1.0)
        self.assertGreaterEqual(agent.tension, 0)

    def test_dimension_contacts(self):
        shadow = ShadowAgent("Senca")
        angel = AngelAgent("Gabriel")
        agent = Agent("A", shadow_agent=shadow, angel_agent=angel)
        self.assertIn("Senca", agent.contact_shadow())
        self.assertIn("Gabriel", agent.contact_angel())


if __name__ == '__main__':
    unittest.main()

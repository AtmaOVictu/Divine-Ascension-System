import unittest
from divine_agents.agent import Agent, VersionedAgent
from divine_agents.dialogue import philosophical_dialogue, interactive_contact_dialogue


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


class TestVersionedAgents(unittest.TestCase):
    def test_version_increment(self):
        a = VersionedAgent("A")
        b = VersionedAgent("B")
        a.contact(b)
        self.assertEqual(a.version, 2)

    def test_contact_transition(self):
        a = VersionedAgent("A", tension=0.6)
        b = VersionedAgent("B")
        a.contact(b)
        self.assertEqual(a.state, "Jaz")

    def test_interactive_contact_dialogue(self):
        a1 = VersionedAgent("A1")
        a2 = VersionedAgent("A2", state="Jaz")
        lines = interactive_contact_dialogue(a1, a2)
        self.assertTrue(any("verzija" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

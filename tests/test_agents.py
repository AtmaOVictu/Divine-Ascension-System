import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.qa_aq import QAAQSystem


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

    def test_qa_aq_interaction(self):
        agent = Agent("B1")
        system = QAAQSystem(agent)
        history = system.interact("Kaj je namen napetosti?")
        self.assertGreaterEqual(len(history), 2)
        self.assertNotEqual(agent.state, "Ego")


if __name__ == '__main__':
    unittest.main()

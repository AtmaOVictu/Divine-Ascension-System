import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.insertion_agent import InsertionAgent


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


class TestInsertionAgent(unittest.TestCase):
    def test_state_and_behavior_insertion(self):
        agent = Agent("A")
        inserter = InsertionAgent(agent)
        inserter.add_state("Transcendence")
        self.assertIn("Transcendence", agent.STATES)

        def custom_response(self, question):
            return "Custom truth"

        inserter.add_behavior("respond", custom_response)
        self.assertEqual(agent.respond("?"), "Custom truth")


if __name__ == '__main__':
    unittest.main()

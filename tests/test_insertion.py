import unittest
from divine_agents.agent import Agent
from divine_agents.insertion_agent import InsertionAgent
from divine_agents.dialogue import dynamic_dialogue


class TestInsertionAgent(unittest.TestCase):
    def test_insert_state(self):
        agent = Agent("A")
        ia = InsertionAgent(agent)
        ia.insert_state("Transcendence")
        self.assertIn("Transcendence", Agent.STATES)

    def test_insert_data(self):
        agent = Agent("B")
        ia = InsertionAgent(agent)
        ia.insert_data({"philosophy": "Existentialism"})
        self.assertEqual(agent.knowledge.get("philosophy"), "Existentialism")

    def test_dynamic_dialogue_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = dynamic_dialogue(a1, a2)
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")
        self.assertTrue(any("Resnica" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

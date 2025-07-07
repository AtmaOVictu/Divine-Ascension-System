import unittest
from divine_agents.agent import Agent
from divine_agents.insertion_agent import InsertionAgent


class TestInsertionAgent(unittest.TestCase):
    def test_insert_state(self):
        agent = Agent("A")
        ins = InsertionAgent(agent)
        ins.insert_state("Jaz")
        self.assertEqual(agent.state, "Jaz")
        self.assertIn("Jaz", agent.history)

    def test_insert_data(self):
        agent = Agent("A")
        ins = InsertionAgent(agent)
        ins.insert_data({"thought": "unity"})
        self.assertTrue(hasattr(agent, "data"))
        self.assertIn({"thought": "unity"}, agent.data)

    def test_modify_behavior(self):
        agent = Agent("A")
        ins = InsertionAgent(agent)

        def new_response(self, question: str) -> str:
            return f"({self.state}) Absolute truth prevails"

        ins.modify_behavior(new_response)
        reply = agent.respond("?")
        self.assertIn("Absolute truth", reply)


if __name__ == "__main__":
    unittest.main()

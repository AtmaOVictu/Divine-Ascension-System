import unittest
import random
from divine_agents.meta import MetaAgent, RandomCodeTester


class TestMetaAgents(unittest.TestCase):
    def test_meta_agent_generates_all_tests(self):
        random.seed(0)
        agent = MetaAgent("M")
        for _ in range(len(agent.known_data)):
            agent.execute_test()
        self.assertEqual(len(agent.get_test_results()), len(agent.known_data))
        result = agent.execute_test()
        self.assertIn("Vsi testi", result)

    def test_random_code_tester_blocks(self):
        random.seed(0)
        tester = RandomCodeTester(["b1", "b2", "b3"])
        for _ in range(3):
            tester.test_random_block()
        self.assertEqual(len(tester.get_tested_blocks()), 3)
        result = tester.test_random_block()
        self.assertIn("Vsi bloki", result)


if __name__ == "__main__":
    unittest.main()

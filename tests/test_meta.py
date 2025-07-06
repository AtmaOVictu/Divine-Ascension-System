import unittest
from divine_agents.meta import MetaAgent, RandomCodeTester

class TestMetaAgent(unittest.TestCase):
    def test_meta_agent_unique_tests(self):
        agent = MetaAgent("Meta", known_data=["A", "B"])
        results = [agent.execute_test() for _ in range(3)]
        self.assertEqual(len(agent.get_test_results()), 2)
        self.assertIn("Vsi testi so že bili izvedeni", results[-1])

class TestRandomCodeTester(unittest.TestCase):
    def test_random_blocks_unique(self):
        tester = RandomCodeTester(["blk1", "blk2"])
        results = [tester.test_random_block() for _ in range(3)]
        self.assertEqual(len(tester.get_tested_blocks()), 2)
        self.assertIn("Vsi bloki so že bili preizkušeni.", results[-1])

if __name__ == '__main__':
    unittest.main()

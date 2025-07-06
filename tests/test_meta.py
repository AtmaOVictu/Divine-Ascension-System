import unittest
from divine_agents.meta import MetaAgent, RandomCodeTester


class TestMetaAgent(unittest.TestCase):
    def test_generate_all_tests(self):
        agent = MetaAgent("meta")
        results = [agent.execute_test() for _ in range(5)]
        self.assertEqual(len(agent.get_test_results()), 5)
        self.assertTrue(all(result is not None for result in results))
        # Exhaustion should return None
        self.assertIsNone(agent.execute_test())


class TestRandomCodeTester(unittest.TestCase):
    def test_blocks_unique(self):
        blocks = ["b1", "b2", "b3"]
        tester = RandomCodeTester(blocks)
        outputs = [tester.test_random_block() for _ in range(3)]
        self.assertEqual(len(tester.get_tested_blocks()), 3)
        self.assertTrue(all(out is not None for out in outputs))
        # After all blocks used, should return None
        self.assertIsNone(tester.test_random_block())


if __name__ == "__main__":
    unittest.main()

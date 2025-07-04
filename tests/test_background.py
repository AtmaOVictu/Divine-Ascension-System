import unittest
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from divine_agents.agent import Agent
from divine_agents.background import generate_background


class TestBackgroundGeneration(unittest.TestCase):
    def test_generate_background_contains_name(self):
        random.seed(0)
        story = generate_background("A")
        self.assertIn("A", story)

    def test_agent_background_created(self):
        random.seed(1)
        agent = Agent("Hero")
        story = agent.create_background()
        self.assertIsNotNone(story)
        self.assertEqual(agent.background, story)
        self.assertIn("Hero", story)


if __name__ == "__main__":
    unittest.main()

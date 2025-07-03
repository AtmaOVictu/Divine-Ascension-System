import unittest
import sys
from pathlib import Path

# Add project root to path so imports work when tests are executed from this directory
sys.path.append(str(Path(__file__).resolve().parents[1]))

from divine_agents.opposite import OppositeAgent


class TestOppositeAgent(unittest.TestCase):
    def test_generate_opposite_when_missing(self):
        agent = OppositeAgent(name="A", symbol="α")
        generated = agent.seek_opposite(environment=None)
        self.assertEqual(generated, "¬α")

    def test_use_existing_opposite(self):
        agent = OppositeAgent(name="A", symbol="β", opposite_symbol="¬β")
        result = agent.seek_opposite(environment=["¬β", "γ"])
        self.assertEqual(result, "¬β")


if __name__ == "__main__":
    unittest.main()

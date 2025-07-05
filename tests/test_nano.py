import unittest
from divine_agents import Agent, Nano


class TestNano(unittest.TestCase):
    def test_nano_application(self):
        agent = Agent("A")
        nano = Nano(emotion_delta=0.6)
        agent.apply_nano(nano)
        # Transition should occur because emotion becomes 0.6
        state = agent.transition()
        self.assertEqual(state, "Jaz")


if __name__ == "__main__":
    unittest.main()

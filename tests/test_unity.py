import unittest
from divine_agents.unity import LoadingScreenUnity, PhilosopherAgent


class TestUnity(unittest.TestCase):
    def test_loading_progress(self):
        loader = LoadingScreenUnity("A", max_value=2)
        loader.transition()
        loader.transition()
        self.assertEqual(loader.unity_value, 2)

    def test_philosopher_enlightenment(self):
        agent = PhilosopherAgent("P", max_value=1)
        agent.transition()
        self.assertEqual(agent.state, "Enlightened")


if __name__ == "__main__":
    unittest.main()

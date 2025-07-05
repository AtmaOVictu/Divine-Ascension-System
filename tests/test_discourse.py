import unittest
from divine_agents.agent import Agent
from divine_agents.discourse import Discourse


class TestDiscourse(unittest.TestCase):
    def test_step_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        disc = Discourse(a1, a2)
        disc.step((0.8, 0.8))
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")

    def test_run_dialogue_content(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        disc = Discourse(a1, a2)
        lines = disc.run([(0.8, 0.8)])
        self.assertTrue(any("Resnica" in line for line in lines))


if __name__ == "__main__":
    unittest.main()

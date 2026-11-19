import unittest
from divine_agents.agent import Agent
from divine_agents.regeneration import Regeneration
from divine_agents.dialogue import regenerative_dialogue


class TestRegeneration(unittest.TestCase):
    def test_death_and_rebirth(self):
        a = Agent("R")
        a.update_emotion(0.8)
        regen = Regeneration(a)
        self.assertEqual(regen.progress(), "⊘")
        self.assertEqual(regen.progress(), "Jaz")

    def test_final_transition(self):
        a = Agent("R", state="Jaz")
        a.update_tension(0.8)
        regen = Regeneration(a)
        self.assertEqual(regen.progress(), "Enotnost")

    def test_dialogue_flow(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = regenerative_dialogue(a1, a2)
        self.assertTrue(any("⊘" in l for l in lines))
        self.assertTrue(any("Jaz" in l for l in lines))


if __name__ == "__main__":
    unittest.main()

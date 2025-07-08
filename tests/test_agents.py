import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import dynamic_dialogue, philosophical_dialogue
from divine_agents.sorting_hat import SortingHatAgent


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dynamic_dialogue_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = dynamic_dialogue(a1, a2, rounds=2)
        self.assertTrue(any("Enotnost" in line for line in lines))


class TestSortingHat(unittest.TestCase):
    def test_sorting_words(self):
        hat = SortingHatAgent("Hat")
        hat.sort("potential")
        hat.sort("truth")
        hat.sort("love")
        boxes = hat.get_sorted_boxes()
        self.assertIn("potential", boxes["Onto"])
        self.assertIn("truth", boxes["Main Branch"])
        self.assertIn("love", boxes["Branches"]["l"])


if __name__ == '__main__':
    unittest.main()

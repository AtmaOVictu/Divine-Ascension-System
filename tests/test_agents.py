import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.box import SymbolicBox


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("A")
        agent.set_emotion("fear", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses_with_emotion(self):
        agent = Agent("A", state="Enotnost")
        agent.set_emotion("joy", 0.4)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("veselje", reply)  # check emotion note
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Expect a transition to occur in dialogue
        self.assertTrue(any("prehaja v stanje" in line for line in lines))
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_box_protection(self):
        box = SymbolicBox(stage="∴", data={"x": 1})
        box.set_protection(True)
        with self.assertRaises(PermissionError):
            box.update_data({"y": 2})


if __name__ == '__main__':
    unittest.main()

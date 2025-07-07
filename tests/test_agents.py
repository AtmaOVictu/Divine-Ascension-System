import unittest
from divine_agents import Agent, philosophical_dialogue, SymbolicBox, EmotionalAgent, EmotionalBox


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
        self.assertTrue(any("Box at stage" in line for line in lines))

    def test_symbolic_box_transitions(self):
        box = SymbolicBox(stage="∴")
        self.assertTrue(box.is_valid_transition("∆"))
        box.transition("∆", {"step": 1})
        self.assertEqual(box.stage, "∆")
        with self.assertRaises(ValueError):
            box.transition("∴", {})

    def test_emotional_box_processing(self):
        e_agent = EmotionalAgent()
        e_box = EmotionalBox("anger")
        status = e_box.process_emotion(e_agent)
        self.assertEqual(status, "Emotion confirmed: Negative")
        result = e_box.transition_emotion(e_agent)
        self.assertEqual(result, "Emotion halted. Task cannot proceed.")


if __name__ == '__main__':
    unittest.main()

import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


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


class TestEmotionalProcessing(unittest.TestCase):
    def test_emotional_box_positive(self):
        from divine_agents.emotion import EmotionalBox, MainTaskAgent
        box = EmotionalBox("joy")
        agent = MainTaskAgent()
        result = agent.handle_task("Analyze", box)
        self.assertIn("completed", result)

    def test_emotional_box_negative(self):
        from divine_agents.emotion import EmotionalBox, MainTaskAgent
        box = EmotionalBox("anger")
        agent = MainTaskAgent()
        result = agent.handle_task("Analyze", box)
        self.assertIn("halted", result)


if __name__ == '__main__':
    unittest.main()

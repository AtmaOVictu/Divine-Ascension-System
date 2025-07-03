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
        prompts = ["Kaj je resnica?"]
        lines = philosophical_dialogue(a1, a2, prompts)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dialogue_custom_prompts_and_emotions(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        prompts = ["Kaj je resnica?", "Ali je resnica absolutna?"]
        lines = philosophical_dialogue(a1, a2, prompts, emotion_increments=(0.9, 0.4))
        self.assertEqual(a1.emotion, 0.9)
        self.assertEqual(a2.emotion, 0.4)
        self.assertTrue(all(any(prompt in line for line in lines) for prompt in prompts))


if __name__ == '__main__':
    unittest.main()

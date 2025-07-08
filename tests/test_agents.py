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
        lines = philosophical_dialogue(a1, a2, 0.8, 0.6)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dialogue_no_transition(self):
        a1 = Agent("B1")
        a2 = Agent("B2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, 0.2, 0.1)
        # Neither agent should reach the next state
        self.assertTrue(all("prehaja v stanje: Ego" in l or "prehaja v stanje: Jaz" in l for l in lines if "prehaja" in l))

    def test_dialogue_with_hook(self):
        a1 = Agent("C1")
        a2 = Agent("C2")

        def custom_line(x, y):
            return f"Custom line between {x.name} and {y.name}"

        lines = philosophical_dialogue(a1, a2, 0.8, 0.8, hooks=[custom_line])
        self.assertTrue(any("Custom line" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

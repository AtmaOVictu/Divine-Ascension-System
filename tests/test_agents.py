import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import (
    philosophical_dialogue,
    apply_emotional_shift,
    handle_state_transition,
    compose_response,
)


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

    def test_helper_functions(self):
        agent = Agent("H")
        apply_emotional_shift(agent, 0.9)
        new_state = handle_state_transition(agent)
        self.assertEqual(new_state, "Jaz")
        line = compose_response(agent, "Kaj je resnica?")
        self.assertIn("Jaz", line)


if __name__ == '__main__':
    unittest.main()

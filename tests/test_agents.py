import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.mediation import Mediator, Meditator


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

    def test_mediator_validation(self):
        agent = Agent("M")
        agent.update_tension(0.8)
        mediator = Mediator(agent)
        result = mediator.validate_command("prehod")
        self.assertIn("uspešno", result)

    def test_meditator_transition(self):
        agent = Agent("X", tension=0.2)
        meditator = Meditator(agent)
        message = meditator.transition_to_peace()
        self.assertIn("Enotnost", message)


if __name__ == '__main__':
    unittest.main()

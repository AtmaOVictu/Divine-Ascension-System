import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.mediator import Mediator
from divine_agents.meditator import Meditator


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


class TestMediatorMeditator(unittest.TestCase):
    def test_mediator_triggers_transition(self):
        agent = Agent("M")
        agent.update_tension(0.8)
        result = agent.mediator.validate_command("prehod")
        self.assertIn("Prehod uspešno", result)
        self.assertEqual(agent.state, "Jaz")

    def test_meditator_peaceful_transition(self):
        agent = Agent("P", tension=0.1)
        message = agent.meditator.transition_to_peace()
        self.assertEqual(agent.state, "Enotnost")
        self.assertIn("Enotnost", message)

    def test_execute_action(self):
        agent = Agent("X")
        agent.update_emotion(0.6)
        msg = agent.execute_action("prehod")
        self.assertIn(agent.state, msg)


if __name__ == '__main__':
    unittest.main()

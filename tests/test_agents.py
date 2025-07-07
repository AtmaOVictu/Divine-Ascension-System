import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.processes import Affirmation, Negation


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

    def test_affirmation_and_negation(self):
        agent = Agent("B")
        msg = Affirmation.affirm_existence(agent)
        self.assertIn("Affirmation", msg)
        agent.update_tension(0.8)
        agent.transition()
        msg = Affirmation.affirm_transition(agent)
        self.assertIn(agent.state, msg)
        Negation.negate_state(agent)
        # after negation from Jaz -> Ego or Ego -> Enotnost
        self.assertIn(agent.state, Agent.STATES)


if __name__ == '__main__':
    unittest.main()

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



class TestMeditationAndMediation(unittest.TestCase):
    def test_meditation_triggers_transition(self):
        agent = Agent("M")
        from divine_agents.processes import Meditacija
        med = Meditacija(agent)
        new_state = med.meditate()
        self.assertEqual(new_state, "Jaz")

    def test_mediation_forces_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        from divine_agents.processes import Mediator
        mediator = Mediator("Med")
        result_state = mediator.mediate(a1, a2)
        self.assertEqual(result_state, "Jaz")

if __name__ == "__main__":
    unittest.main()


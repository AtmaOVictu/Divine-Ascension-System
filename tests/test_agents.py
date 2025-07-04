import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.phases import RESPhase


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

    def test_phase_transition(self):
        phase = RESPhase(label="RES000", tension=0.8)
        self.assertTrue(phase.transition())
        self.assertEqual(phase.emotion, "Transformed Emotion")

    def test_agent_phase_modification(self):
        phase = RESPhase(label="RES000")
        agent = Agent("A", phase=phase)
        agent.modify_phase(new_emotion="Joy", new_tension=0.9, new_gift="Insight")
        self.assertEqual(agent.phase.emotion, "Joy")
        self.assertEqual(agent.phase.tension, 0.9)


if __name__ == '__main__':
    unittest.main()

import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        with self.assertLogs('divine_agents.agent', level='INFO') as cm:
            agent.update_tension(0.8)
            state = agent.transition()
        self.assertEqual(state, "Jaz")
        log_text = " ".join(cm.output)
        self.assertIn('tension set to', log_text)
        self.assertIn('transitioned from Ego to Jaz', log_text)

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        with self.assertLogs('divine_agents.agent', level='DEBUG') as cm:
            reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn('responds', " ".join(cm.output))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        with self.assertLogs('divine_agents.dialogue', level='DEBUG') as cm:
            lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertIn('Starting dialogue', " ".join(cm.output))


if __name__ == '__main__':
    unittest.main()

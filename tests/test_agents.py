import unittest
from divine_agents import Agent, SubAgent, philosophical_dialogue


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

    def test_sub_agent_logging(self):
        agent = Agent("Log")
        sa = SubAgent("logger", agent)
        agent.add_sub_agent(sa)
        agent.update_emotion(0.9)
        agent.transition()
        self.assertTrue(any("Emotion updated" in log for log in sa.logs))
        self.assertTrue(any("State transitioned" in log for log in sa.logs))
        # Ensure logs are sorted
        sorted_logs = sa.sort_logs()
        self.assertEqual(sorted_logs, sorted(sa.logs, key=lambda x: x.split(' - ')[0]))


if __name__ == '__main__':
    unittest.main()

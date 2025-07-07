import unittest
from divine_agents.agent import Agent
from divine_agents.sub_agent import SubAgent
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

    def test_sub_agent_logging(self):
        agent = Agent("A")
        sub = SubAgent("SA", agent)
        agent.add_sub_agent(sub)
        agent.update_tension(0.9)
        agent.transition()
        self.assertTrue(any("State transitioned" in log for log in sub.logs))

    def test_log_sorting(self):
        agent = Agent("A")
        sub = SubAgent("SA", agent)
        agent.add_sub_agent(sub)
        agent.update_emotion(0.6)
        agent.respond("Kaj je resnica?")
        unsorted = list(sub.logs)
        sorted_logs = sub.sort_logs()
        self.assertEqual(sorted_logs, sorted(unsorted))


if __name__ == '__main__':
    unittest.main()

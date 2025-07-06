import unittest
from divine_agents import Agent, run_debate

class TestDebateModule(unittest.TestCase):
    def test_run_debate_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        transcript = run_debate(a1, a2, rounds=2)
        # after two rounds tension should push at least one agent beyond Ego
        self.assertIn("prehaja v stanje", " ".join(transcript))
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)

if __name__ == "__main__":
    unittest.main()

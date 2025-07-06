import unittest
from divine_agents.agent import Agent
from divine_agents.tracker import OntologicalTracker


class TestOntologicalTracker(unittest.TestCase):
    def test_debate_and_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        tracker = OntologicalTracker([a1, a2])
        lines = tracker.initiate_debate("A1", "A2", "Kaj je resnica?")
        # check dialogue content
        self.assertIn("absolutna", lines[0])
        self.assertIn("relativna", lines[1])
        # at least one transition should be recorded
        self.assertTrue(tracker.transitions)
        # final states should reflect possible transitions
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)


if __name__ == "__main__":
    unittest.main()

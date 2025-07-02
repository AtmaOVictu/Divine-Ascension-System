import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
import random
from divine_agents import (
    Agent,
    philosophical_dialogue,
    MutatingAgent,
    PermutingAgent,
    InspirationalAgent,
    EthicalChallenge,
)


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


class TestAdvancedAgents(unittest.TestCase):
    def test_mutation(self):
        agent = MutatingAgent("M")
        # Force mutation by patching random.random
        original_random = random.random
        random.random = lambda: 0.1
        agent.mutate()
        random.random = original_random
        self.assertIn(agent.state, Agent.STATES)

    def test_permutation(self):
        a1 = MutatingAgent("A1", philosophy="Stoicizem")
        a2 = MutatingAgent("A2", philosophy="Empirizem")
        perm = PermutingAgent(a1, a2)
        perm.permute()
        self.assertEqual(a1.philosophy, "Empirizem")
        self.assertEqual(a2.philosophy, "Stoicizem")

    def test_inspiration_and_ethics(self):
        inspirer = InspirationalAgent("I", inspiration=True)
        target = MutatingAgent("T", state="Ego")
        inspirer.inspire(target)
        self.assertIn(target.state, {"Jaz", "Enotnost"})
        challenge = EthicalChallenge(
            "Dilema",
            ["Svoboda", "Harmonija"],
            target,
        )
        decision = challenge.present()
        self.assertIn(decision, {"Svoboda", "Harmonija"})
        self.assertIn(target.state, {"Ego", "Enotnost"})


if __name__ == "__main__":
    unittest.main()

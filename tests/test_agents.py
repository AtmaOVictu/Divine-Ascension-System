import os
import tempfile
import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.file_renamer import FileRenamingAgent
from divine_agents.archetype import ArchetypeAgent


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


class TestFileRenamingAgent(unittest.TestCase):
    def test_rename_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = os.path.join(tmp, "a.py")
            dst = os.path.join(tmp, "b.py")
            open(src, "w").close()
            agent = FileRenamingAgent("renamer")
            success = agent.rename_file(src, dst)
            self.assertTrue(success)
            self.assertTrue(os.path.exists(dst))


class TestArchetypeAgent(unittest.TestCase):
    def test_evolve_and_influence(self):
        archetype = ArchetypeAgent("Truth", "Absolute Truth")
        msg1 = archetype.influence_environment()
        archetype.update_emotion(0.9)
        archetype.evolve("Ego")
        msg2 = archetype.influence_environment()
        self.assertIn("temelj", msg1)
        self.assertIn("individualnost", msg2)


if __name__ == "__main__":
    unittest.main()

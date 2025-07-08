import unittest
import os
import tempfile
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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

    def test_file_renamer(self):
        agent = FileRenamingAgent("Renamer")
        with tempfile.TemporaryDirectory() as tmp:
            src = os.path.join(tmp, "a.py")
            dst = os.path.join(tmp, "b.py")
            open(src, "w").close()
            self.assertTrue(agent.rename_file(src, dst))
            self.assertTrue(os.path.exists(dst))

    def test_archetype_agent(self):
        agent = ArchetypeAgent("Alpha", archetype_type="Ego")
        agent.update_emotion(0.6)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")
        message = agent.influence_environment()
        self.assertIn("individualnost", message)


if __name__ == '__main__':
    unittest.main()

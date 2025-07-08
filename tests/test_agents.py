import os
import tempfile
import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.renamer import FileRenamingAgent
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
        # Expect transition to at least Jaz or Enotnost
        self.assertTrue(any("Jaz" in line or "Enotnost" in line for line in lines))

    def test_file_renaming_agent(self):
        agent = FileRenamingAgent("Renamer")
        with tempfile.TemporaryDirectory() as tmpdir:
            src = os.path.join(tmpdir, "old.py")
            dst = os.path.join(tmpdir, "new.py")
            with open(src, "w") as f:
                f.write("print('x')")
            self.assertTrue(agent.rename_file(src, dst))
            self.assertTrue(os.path.exists(dst))

    def test_archetype_evolution(self):
        archetype = ArchetypeAgent("Truth", "Absolute Truth")
        self.assertEqual(archetype.influence_environment(), "Truth razkriva temelj resničnosti.")
        archetype.evolve("Ego")
        self.assertEqual(archetype.archetype_type, "Ego")
        self.assertEqual(archetype.power, 150)


if __name__ == "__main__":
    unittest.main()

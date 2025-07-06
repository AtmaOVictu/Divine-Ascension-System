import unittest

from divine_agents import Agent, DialogueManager


class TestDialogueManager(unittest.TestCase):
    def test_step_triggers_transition(self):
        a1 = Agent("A1", tension=0.0, emotion=0.4)
        a2 = Agent("A2", state="Jaz", tension=0.0, emotion=0.4)
        manager = DialogueManager(a1, a2)
        lines = manager.step()
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)
        self.assertTrue(any("prehaja v stanje" in l for l in lines))
        self.assertNotEqual(a1.state, "Ego")  # should move to Jaz

    def test_run_dialogue_content(self):
        a1 = Agent("A1", emotion_type="fear")
        a2 = Agent("A2", state="Jaz", emotion_type="joy")
        manager = DialogueManager(a1, a2)
        transcript = manager.run(steps=2)
        joined = "\n".join(transcript)
        self.assertIn("absolutna", joined)
        self.assertIn("relativna", joined)
        self.assertTrue(a2.state in ("Jaz", "Enotnost"))


if __name__ == "__main__":
    unittest.main()

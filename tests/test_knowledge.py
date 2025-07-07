import unittest
from divine_agents.knowledge import (
    LukaKnowledgeBox,
    CodexWithLukaKnowledge,
    EmotionalAgent,
    EmotionalBox,
)


class TestKnowledgeIntegration(unittest.TestCase):
    def test_unpack_luka_knowledge(self):
        box = LukaKnowledgeBox(concept="Time", explanation="Progression of events")
        data = box.unpack_knowledge()
        self.assertEqual(data["concept"], "Time")

    def test_codex_process_knowledge(self):
        codex = CodexWithLukaKnowledge()
        box = LukaKnowledgeBox(concept="Existence", explanation="State of being")
        codex.add_knowledge(box)
        processed = codex.process_knowledge()
        self.assertIn("Existence", processed[0]["concept"])

    def test_emotional_box_processing(self):
        agent = EmotionalAgent("EA")
        box = EmotionalBox("joy")
        result = box.process_emotion(agent)
        self.assertEqual(result, "Emotion confirmed: Positive")


if __name__ == "__main__":
    unittest.main()

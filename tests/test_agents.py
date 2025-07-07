import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.symbolic import initiate_task, process_task, resolve_task, SymbolicBox


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
        box = philosophical_dialogue(a1, a2)
        lines = box.get_data()["dialogue"]
        self.assertEqual(box.stage, "⊘")
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_emotional_response(self):
        agent = Agent("A")
        agent.update_emotion(0.6, "fear")
        agent.transition()
        self.assertEqual(agent.state, "Jaz")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("strah", reply)

    def test_symbolic_box_workflow(self):
        box = initiate_task("demo")
        self.assertEqual(box.stage, "∴")
        box = process_task(box, {"step": 1})
        self.assertEqual(box.stage, "∆")
        box = resolve_task(box)
        self.assertEqual(box.stage, "⊘")


if __name__ == '__main__':
    unittest.main()

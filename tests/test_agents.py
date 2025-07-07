import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.box import (
    SymbolicBox,
    SelfBoxedAgent,
    RecursiveTaskBox,
    RecursiveSelfReflectionAgent,
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

    def test_symbolic_box(self):
        box = SymbolicBox(stage="∴", data={"a": 1})
        box.transition("∆", {"b": 2})
        self.assertEqual(box.stage, "∆")
        self.assertEqual(box.get_data()["b"], 2)

    def test_self_boxed_agent(self):
        agent = SelfBoxedAgent("Codex")
        agent.process_task("Test")
        self.assertEqual(agent.self_box.stage, "⊘")
        self.assertEqual(agent.self_box.get_data()["state"], "completed")

    def test_recursive_self_reflection_agent(self):
        agent = RecursiveSelfReflectionAgent("Codex")
        agent.process_task_with_reflection("Quest")
        reflection = agent.reflect_on_task()
        self.assertIn("Codex", reflection)


if __name__ == '__main__':
    unittest.main()

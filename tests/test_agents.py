import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

from divine_agents.tasks import Task, TaskAgent, SystemErrorAgent, UrgentDecisionAgent

class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.9, "fear")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("intenzivna", reply)
        self.assertIn("fear", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("anger" in line for line in lines))

    def test_no_transition_below_thresholds(self):
        agent = Agent("B")
        agent.update_tension(0.4)
        agent.update_emotion(0.3)
        state = agent.transition()
        self.assertEqual(state, "Ego")



class TestTaskAgents(unittest.TestCase):
    def test_execute_tasks_triggers_transition(self):
        base = Agent('T')
        task_agent = TaskAgent(base)
        task_agent.add_task(Task('urgent', 0.9))
        state = task_agent.execute_tasks()
        self.assertEqual(state, 'Jaz')

    def test_system_error_causes_state_change(self):
        base = Agent('S')
        err_agent = SystemErrorAgent(base, system_error=True)
        state = err_agent.check_system()
        self.assertEqual(state, 'Jaz')

    def test_urgent_decision_sets_enotnost(self):
        base = Agent('U')
        urgent = UrgentDecisionAgent(base)
        state = urgent.make_urgent_decision()
        self.assertEqual(state, 'Enotnost')

if __name__ == "__main__":
    unittest.main()

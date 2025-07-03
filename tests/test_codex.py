import unittest

from divine_agents.config import CodexConfig
from divine_agents.codex_agent import CodexAgent
from divine_agents.codex_dialogue import dynamic_dialogue


class TestCodexAgents(unittest.TestCase):
    def test_config_load(self):
        config = CodexConfig('settings.json')
        agents = config.instantiate_agents()
        self.assertEqual(len(agents), 2)
        self.assertEqual(agents[0].ime, 'Agent1')

    def test_state_transition(self):
        agent = CodexAgent('T', 'Stoicism', 'Self', 'Ego')
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, 'Jaz')

    def test_dynamic_dialogue(self):
        config = CodexConfig('settings.json')
        a1, a2 = config.instantiate_agents()
        lines = dynamic_dialogue(a1, a2)
        self.assertTrue(any('Enotnost' in line for line in lines))


if __name__ == '__main__':
    unittest.main()

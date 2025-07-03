import unittest
from io import StringIO
from unittest.mock import patch

from divine_agents.knowledge_base import KnowledgeBase


class TestKnowledgeBase(unittest.TestCase):
    def setUp(self):
        self.kb = KnowledgeBase()

    def test_copy_from_library(self):
        tasks = self.kb.copy_from_library('naloge')
        self.assertIn('samospoznanje', tasks)
        self.assertIsInstance(tasks, list)
        tasks.append('nova')
        self.assertNotIn('nova', self.kb.library['naloge'])

    def test_print_from_library(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_out:
            self.kb.print_from_library('nujnosti')
            output = mock_out.getvalue()
            self.assertIn('kritična napaka', output)


if __name__ == '__main__':
    unittest.main()

import subprocess
import sys
import unittest


class TestCLI(unittest.TestCase):
    def test_cli_runs(self):
        cmd = [
            sys.executable,
            '-m', 'divine_agents.cli',
            '--name1', 'A1', '--state1', 'Ego', '--tension1', '0.8', '--emotion1', '0.6',
            '--name2', 'A2', '--state2', 'Jaz', '--tension2', '0.0', '--emotion2', '0.0'
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout
        self.assertIn('A1', output)
        self.assertIn('A2', output)
        self.assertEqual(result.returncode, 0)


if __name__ == '__main__':
    unittest.main()

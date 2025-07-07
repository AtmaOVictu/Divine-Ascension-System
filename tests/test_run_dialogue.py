import unittest
from unittest.mock import patch

from divine_agents import run_dialogue


class TestRunDialogue(unittest.TestCase):
    def test_cli_runs(self):
        test_args = [
            "--name1",
            "Ana",
            "--name2",
            "Boris",
            "--state1",
            "Ego",
            "--state2",
            "Jaz",
        ]
        with patch("sys.argv", ["run_dialogue"] + test_args):
            # Capture printed lines
            with patch("builtins.print") as mock_print:
                run_dialogue.main()
                self.assertTrue(mock_print.called)
                # Ensure dialogue generated at least one line referencing states
                printed = " ".join(str(args[0]) for args, _ in mock_print.call_args_list)
                self.assertIn("Ego", printed)
                self.assertIn("Jaz", printed)


if __name__ == "__main__":
    unittest.main()

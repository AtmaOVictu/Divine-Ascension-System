import unittest
import tempfile
import time
import logging
from pathlib import Path
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
try:
    from divine_agents.watch import Watcher
    import watchdog
except Exception:  # watchdog not installed
    Watcher = None
    watchdog = None


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

    @unittest.skipIf(Watcher is None, "watchdog not installed")
    def test_watcher_detects_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            log_file = Path(tmp) / "log.txt"
            # Configure logger for temporary log
            from divine_agents import logger
            for h in list(logger.handlers):
                logger.removeHandler(h)
            handler = logging.FileHandler(log_file)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)

            watched_file = Path(tmp) / "test.txt"
            watched_file.write_text("initial")

            watcher = Watcher(tmp)
            watcher.start()
            try:
                time.sleep(0.2)
                watched_file.write_text("changed")
                time.sleep(1)
            finally:
                watcher.stop()

            content = log_file.read_text()
            self.assertIn("Modified", content)


if __name__ == '__main__':
    unittest.main()

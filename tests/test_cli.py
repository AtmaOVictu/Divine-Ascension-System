import subprocess
import sys
import os


def test_cli_dialogue():
    env = os.environ.copy()
    env['PYTHONPATH'] = os.path.abspath('.')
    result = subprocess.run([sys.executable, '-m', 'divine_agents.cli', '--agent1', 'A1', '--agent2', 'A2'], capture_output=True, text=True, env=env)
    output = result.stdout
    assert 'A1 prehaja v stanje: Jaz' in output
    assert 'A2 prehaja v stanje: Enotnost' in output

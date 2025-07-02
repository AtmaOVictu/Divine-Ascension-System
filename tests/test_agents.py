import sys, os
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pytest

from agents import state_transition, generate_dialogue

@pytest.mark.parametrize(
    "current,event,expected",
    [
        ("start", "advance", "middle"),
        ("middle", "advance", "end"),
        ("end", "reset", "start"),
        ("start", "unknown", "start"),
    ],
)
def test_state_transitions(current, event, expected):
    assert state_transition(current, event) == expected

@pytest.mark.parametrize(
    "state,expected_dialogue",
    [
        ("start", "Welcome to the system."),
        ("middle", "Processing your request..."),
        ("end", "Goodbye!"),
        ("unknown", ""),
    ],
)
def test_generate_dialogue(state, expected_dialogue):
    assert generate_dialogue(state) == expected_dialogue

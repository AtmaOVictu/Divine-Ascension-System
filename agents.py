"""Simple state machine for demonstration purposes."""

from typing import Dict, Tuple

# Transition map: (current_state, event) -> next_state
_TRANSITIONS: Dict[Tuple[str, str], str] = {
    ("start", "advance"): "middle",
    ("middle", "advance"): "end",
    ("end", "reset"): "start",
}

# Dialogue map per state
_DIALOGUES: Dict[str, str] = {
    "start": "Welcome to the system.",
    "middle": "Processing your request...",
    "end": "Goodbye!",
}

def state_transition(current_state: str, event: str) -> str:
    """Return the next state for a given current state and event.

    If the transition is not defined, return the current state.
    """
    return _TRANSITIONS.get((current_state, event), current_state)

def generate_dialogue(state: str) -> str:
    """Return a dialogue response associated with a state."""
    return _DIALOGUES.get(state, "")

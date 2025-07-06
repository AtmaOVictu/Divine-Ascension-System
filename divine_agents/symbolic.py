# Define unicode symbols used to represent tension and emotion
TENSION = 'τ'
EMOTION = 'ϵ'


def check_transition(tension: float, emotion: float) -> bool:
    """Return True if a state transition should occur."""
    return tension > 0.7 or emotion > 0.5


def transition_to_symbol(tension: float, emotion: float) -> str:
    """Return an ontological symbol based on tension and emotion."""
    if check_transition(tension, emotion):
        if tension > emotion:
            return "⊕ (Transcendence - Ego to Jaz)"
        else:
            return "⊗ (Balance - Jaz to Enotnost)"
    return "No transition, remains in current state"

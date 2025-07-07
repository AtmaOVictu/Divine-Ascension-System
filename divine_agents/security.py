"""Security utilities for validating data and transitions."""
import logging
import uuid

logging.basicConfig(filename='codex_errors.log', level=logging.INFO)

STATES = ("Ego", "Jaz", "Enotnost")


def validate_agent_data(name: str, state: str) -> None:
    """Validate initialization data for an Agent."""
    if not isinstance(name, str):
        raise ValueError("Agent name must be a string.")
    if state not in STATES:
        raise ValueError(f"Invalid state '{state}'.")


def check_stage_transition(current: str, nxt: str) -> None:
    """Ensure transitions follow the allowed order."""
    allowed = {"Ego": "Jaz", "Jaz": "Enotnost", "Enotnost": None}
    if allowed.get(current) != nxt:
        raise ValueError("Invalid transition.")


def sanitize_output(text: str) -> str:
    """Sanitize output to avoid injection of unwanted characters."""
    return text.replace("<", "&lt;").replace(">", "&gt;")


def log_error(message: str) -> None:
    """Log an error message."""
    logging.error(message)


def generate_ephemeral_token() -> str:
    """Generate a short-lived token."""
    return str(uuid.uuid4())

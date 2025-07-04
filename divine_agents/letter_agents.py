from .agent import Agent


def create_letter_agents(text: str):
    """Create an Agent instance for each alphabetic character."""
    return [Agent(letter.upper()) for letter in text if letter.isalpha()]

class KvizZabavnost:
    """Simple quiz game about ontological transitions."""

    def __init__(self):
        self.questions = [
            {
                "question": "Kaj pomeni prehod iz Ego v Jaz?",
                "answers": ["Sprejemanje", "Prekinitev", "Sprememba"],
                "correct": "Sprejemanje",
            },
            {
                "question": "Kaj je resnica v ontoloskem sistemu?",
                "answers": ["Samospoznanje", "Fizikalna resnicnost", "Absolutna gotovost"],
                "correct": "Samospoznanje",
            },
            {
                "question": "Kaj pomeni prehod iz Enotnosti v Ego?",
                "answers": ["Znova manifestiranje", "Zavracanje realnosti", "Transformacija"],
                "correct": "Znova manifestiranje",
            },
        ]

    def get_random_question(self):
        """Return a random question dictionary."""
        import random

        return random.choice(self.questions)

    def check_answer(self, question: dict, index: int) -> bool:
        """Check whether selected answer index is correct."""
        try:
            return question["answers"][index] == question["correct"]
        except (IndexError, KeyError):
            return False


class UgankaZabavnost:
    """Puzzle encouraging ontological thinking."""

    def __init__(self):
        self.puzzle = "Kaj se zgodi, ko Ego preide v Jaz, vendar ne doseze Enotnosti?"
        self.solution = "Napetost v prehodu"

    def check_solution(self, answer: str) -> bool:
        """Validate puzzle solution."""
        return answer.strip().lower() == self.solution.lower()


class IgraOdlocanja:
    """Decision game influencing agent tension and state."""

    def __init__(self, agent):
        self.agent = agent

    def make_decision(self, decision: bool) -> str:
        """Apply decision to agent and return new state."""
        if decision:
            # Positive decision increases emotion which also raises tension.
            self.agent.update_emotion(0.6)
        else:
            # Negative decision calms the agent slightly.
            new_tension = max(self.agent.tension - 0.3, 0.0)
            self.agent.update_tension(new_tension)
        return self.agent.transition()

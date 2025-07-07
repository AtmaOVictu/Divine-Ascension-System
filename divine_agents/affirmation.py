class SubtleAffirmation:
    """Provide subtle confirmations for internal processes."""

    @staticmethod
    def affirm_emotion_update(agent):
        """Return a short affirmation after an emotion update."""
        return f"Subtle affirmation: {agent.name} is now in {agent.state} with emotion {agent.emotion}."

    @staticmethod
    def affirm_dialogue_progress(log):
        """Append a gentle affirmation to the dialogue log."""
        log.append("Subtle affirmation: Dialogue continues to evolve.")
        return log


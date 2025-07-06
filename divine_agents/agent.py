class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Starting state of the agent. One of ``"Ego"``, ``"Jaz"`` or
        ``"Enotnost"``.
    tension:
        Initial level of tension.
    emotion:
        Initial emotional intensity.

    Attributes
    ----------
    history:
        List of states the agent has occupied.

    Examples
    --------
    >>> agent = Agent("A")
    >>> agent.update_emotion(0.6)
    >>> agent.transition()
    'Jaz'
    """

    # Possible states an agent can occupy.
    #   Ego      : Truth is absolute and independent of others.
    #   Jaz      : Truth is relative and shaped by relationships.
    #   Enotnost : All truths are unified and interconnected.
    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotional intensity on a scale from 0 to 1.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Parameters
        ----------
        value:
            New tension value on a scale from 0 to 1.
        """
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition when thresholds are exceeded.

        Returns
        -------
        str
            The new state of the agent after the transition.
        """
        # Transition criteria: tension above 0.7 or emotion above 0.5
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state.

        Parameters
        ----------
        question:
            The incoming question or statement.

        Returns
        -------
        str
            A response that reflects the agent's ontological stance.
        """
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

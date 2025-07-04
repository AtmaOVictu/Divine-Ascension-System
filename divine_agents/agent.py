class Agent:
    """Represents an ontological agent capable of transitioning states and
    interacting with other agents over a network."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.connected = False

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def connect(self) -> None:
        """Connect the agent to the network."""
        self.connected = True

    def sync_with(self, other: "Agent") -> bool:
        """Synchronize tension and emotion with another agent if both are connected."""
        if self.connected and other.connected:
            avg_tension = (self.tension + other.tension) / 2
            avg_emotion = (self.emotion + other.emotion) / 2
            self.tension = other.tension = avg_tension
            self.emotion = other.emotion = avg_emotion
            return True
        return False

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            mood = " Čustveno sem zelo vznemirjen."
        elif self.emotion > 0.3:
            mood = " Čutim rahlo napetost."
        else:
            mood = ""
        return base + mood

    def commit_to_github(self, message: str) -> None:
        """Attempt to commit the current state of the repository to GitHub."""
        import subprocess

        try:
            subprocess.run(["git", "add", "-A"], check=True)
            subprocess.run(["git", "commit", "-m", message], check=True)
            subprocess.run(["git", "push"], check=True)
        except subprocess.CalledProcessError:
            print(f"{self.name}: GitHub commit failed.")

class Agent:
    """Represents an ontological agent with emotional state and tension."""

    def __init__(self, name, state="Ego", tension=0.0, emotion=0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.stability = 0
        self.environment_change = None

    def transition(self):
        """Update state based on current tension and emotion."""
        if self.tension > 0.7 or self.emotion > 0.8:
            if self.state == "Ego":
                self.state = "Jaz"
                self.stability = 1
            elif self.state == "Jaz":
                self.state = "Enotnost"
                self.stability = 2
        else:
            self.state = "Stabilnost"
            self.stability = 0

    def update_tension(self, new_tension):
        self.tension = new_tension
        self.transition()

    def update_emotion(self, new_emotion):
        self.emotion = new_emotion
        self.transition()

    def update_environment(self, change):
        self.environment_change = change
        self.transition()

    def dialogue(self):
        """Return a dialogue line representing the agent's perspective on truth."""
        if self.state == "Ego":
            return f"{self.name} (Ego): The truth is absolute. It is what I believe, and nothing else matters."
        if self.state == "Jaz":
            return f"{self.name} (Jaz): The truth is relative, shaped by our relationships and interactions with others."
        if self.state == "Enotnost":
            return f"{self.name} (Enotnost): All truths are one. Separation between truths is an illusion."
        return f"{self.name}: I am in a state of uncertainty, unable to define the truth right now."

    def interact(self, other_agents, conversation_topic="philosophy"):
        """Interact with other agents, adjusting tension and emotion."""
        responses = []
        for agent in other_agents:
            if agent is self:
                continue
            if conversation_topic == "philosophy":
                if self.state == "Ego" and agent.state == "Jaz":
                    self.tension += 0.2
                    self.emotion += 0.3
                elif self.state == "Jaz" and agent.state == "Ego":
                    self.tension += 0.3
                    self.emotion += 0.2
                elif self.state == "Enotnost" and agent.state != "Enotnost":
                    self.tension = max(0.0, self.tension - 0.2)
                    self.emotion = max(0.0, self.emotion - 0.1)
                else:
                    self.tension += 0.1
            responses.append(self.dialogue())
            responses.append(agent.dialogue())
        self.update_tension(self.tension)
        self.update_emotion(self.emotion)
        return "\n".join(responses)

    def __str__(self):
        return (
            f"Agent {self.name}: State={self.state}, "
            f"Tension={self.tension}, Emotion={self.emotion}, Stability={self.stability}"
        )

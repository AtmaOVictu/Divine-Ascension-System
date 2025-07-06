class DynamicAgent:
    """Agent with dynamic state transitions and connections."""

    def __init__(self, name, state="neutral", tension=0.0, emotion=0.0, aktivnosti=0):
        self.name = name
        self.state = state
        self.tension = float(tension)
        self.emotion = float(emotion)
        self.aktivnosti = int(aktivnosti)
        self.povezave = []

    def prehod(self):
        """Transition state based on tension and emotion."""
        if self.tension > 0.7:
            self.state = "Jaz"
        elif self.emotion > 0.5:
            self.state = "Enotnost"
        else:
            self.state = "Ego"
        return self.state

    def komunikacija(self, drugi_agent):
        """Communicate with another agent and activate them if necessary."""
        if self.state == "aktiviran":
            drugi_agent.state = "aktiviran"
        
    def reorganiziraj(self, drugi_agent):
        """Automatically reorganize connections when activity threshold is met."""
        if self.aktivnosti > 5:
            self.state = "prehod"
            if self not in drugi_agent.povezave:
                drugi_agent.povezave.append(self)


def dinamicka_inicializacija(agenti):
    """Dynamically connect active agents."""
    for i in range(len(agenti)):
        for j in range(i + 1, len(agenti)):
            a1, a2 = agenti[i], agenti[j]
            if a1.state == "aktiviran" and a2.state == "aktiviran":
                a1.komunikacija(a2)
                a1.reorganiziraj(a2)
                a2.reorganiziraj(a1)
    return agenti


def reorganizacija_sistema(agenti):
    """Increase activity counters and reorganize when high activity is reached."""
    for agent in agenti:
        agent.aktivnosti += 1
        if agent.aktivnosti > 10:
            agent.state = "reorganizirano"
    return agenti

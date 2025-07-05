class Mediator:
    """Coordinates command validation and agent transitions."""
    def __init__(self, agent):
        self.agent = agent

    def validate_command(self, command: str) -> str:
        if command == "prehod":
            return self.check_conditions_for_transition()
        if command == "respond":
            return self.agent.respond("Kaj je resnica?")
        return "Ukaz ni veljaven."

    def check_conditions_for_transition(self) -> str:
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            self.agent.transition()
            return f"Prehod uspešno izveden: {self.agent.state}"
        return "Pogoji za prehod niso izpolnjeni."


class Meditator:
    """Enables self-reflection and awareness for an agent."""
    def __init__(self, agent):
        self.agent = agent

    def self_reflection(self) -> None:
        print(f"Trenutno stanje: {self.agent.state}")
        print(f"Napetost: {self.agent.tension}, Čustva: {self.agent.emotion}")

    def transition_to_peace(self) -> str:
        if self.agent.tension < 0.3:
            self.agent.state = "Enotnost"
            return "Agent prehaja v stanje Enotnost."
        return "Prehodi so potrebni, da dosežeš notranje ravnovesje."

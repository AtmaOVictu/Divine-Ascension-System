class Mediator:
    """Posrednik za usklajevanje prehodov in validacijo ukazov."""

    def __init__(self, agent):
        self.agent = agent

    def validate_command(self, command: str) -> str:
        """Preveri veljavnost ukaza pred izvedbo."""
        if command == "prehod":
            return self.check_conditions_for_transition()
        if command == "respond":
            return self.agent.respond("Kaj je resnica?")
        return "Ukaz ni veljaven."

    def check_conditions_for_transition(self) -> str:
        """Preveri, ali so izpolnjeni pogoji za prehod."""
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            state = self.agent.transition()
            return f"Prehod uspešno izveden: {state}"
        return "Pogoji za prehod niso izpolnjeni."


class Meditator:
    """Meditator za samorefleksijo in notranje zavedanje agenta."""

    def __init__(self, agent):
        self.agent = agent

    def self_reflection(self) -> str:
        """Sporoči trenutno stanje, napetost in čustva."""
        return (
            f"Trenutno stanje: {self.agent.state}, "
            f"Napetost: {self.agent.tension}, "
            f"Čustva: {self.agent.emotion}"
        )

    def transition_to_peace(self) -> str:
        """Omogoči prehod agenta v stanje harmonije, ko so pogoji izpolnjeni."""
        if self.agent.tension < 0.3:
            self.agent.state = "Enotnost"
            self.agent.history.append(self.agent.state)
            return "Agent prehaja v stanje Enotnost."
        return "Prehodi so potrebni, da dosežeš notranje ravnovesje."

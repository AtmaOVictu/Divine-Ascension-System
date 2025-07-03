from .agent import Agent

class SelfDeceptionAgent(Agent):
    """Agent that prefers comforting lies to genuine change."""

    def rationalize(self) -> str:
        """Produce a comforting lie and reduce tension."""
        self.tension *= 0.5
        return "Raje ostanem v tem stanju, resnica je prevec zahtevna."

    def transition(self) -> str:
        """Override to resist change unless tension/emotion very high."""
        if self.tension > 1.0 or self.emotion > 0.9:
            return super().transition()
        self.rationalize()
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        base = super().respond(question)
        if self.state == "Ego":
            return base + " A raje ne razmisljam prevec o spremembi."
        if self.state == "Jaz":
            return base + " A morda sprememba ni potrebna."
        return base

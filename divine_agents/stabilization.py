class NujnaSenca:
    """Represents an urgent shadow influencing agent tension."""

    def __init__(self, ime: str, nujnost: float):
        self.ime = ime
        self.nujnost = nujnost

    def prehod_v_senco(self, agent: 'Agent') -> str:
        if self.nujnost >= 0.8:
            agent.update_tension(agent.tension + self.nujnost)
            agent.transition()
            return f"{agent.name} prehaja v nujno fazo sence: {self.ime}"
        return f"{agent.name} ni v nujni situaciji, ohranja stabilnost."


class DrugaPravaOs:
    """Represents a second true axis guiding the agent."""

    def __init__(self, ime: str, oscilacija: float):
        self.ime = ime
        self.oscilacija = oscilacija
        self.smer = "nevtralna"

    def doloci_smer(self, agent: 'Agent') -> str:
        if self.oscilacija > 0.5:
            self.smer = "proaktivna"
            agent.update_emotion(agent.emotion + self.oscilacija)
        else:
            self.smer = "defenzivna"
            agent.update_tension(agent.tension + (1 - self.oscilacija))
        return self.smer


class NucnoNiclo:
    """Represents the zero state providing stabilization."""

    def __init__(self):
        self.stanje = "mirno"

    def stabilizacija(self) -> str:
        self.stanje = "stabilno"
        return "Sistem je stabiliziran v ničelnem stanju, pred aktivacijo."

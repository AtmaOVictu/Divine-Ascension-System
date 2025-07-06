class AgentTenzije:
    """Classifies expressions into types or forms of tension."""

    def __init__(self):
        self.vrste = []
        self.oblike = []

    def interpretiraj(self, izraz: str) -> str:
        lower = izraz.lower()
        if any(x in lower for x in ["ritem", "ponavljanje", "val", "frekvenca"]):
            self.vrste.append(izraz)
            return "vrsta tenzije – ciklicna napetost"
        if any(x in lower for x in ["trganje", "prelom", "eksplozija", "napet udarec"]):
            self.oblike.append(izraz)
            return "oblika tenzije – singularen preboj"
        return "neopredeljena napetost"

    def porocilo(self) -> dict:
        return {"Vrste": self.vrste, "Oblike": self.oblike}


class AgentSpoznanja:
    """Tracks whether a realization is new or repeated."""

    def __init__(self):
        self.prepoznana = []
        self.ponovitve = []

    def preveri(self, vsebina: str) -> str:
        if vsebina in self.prepoznana:
            self.ponovitve.append(vsebina)
            return "ponovitev spoznanja – notranji odmev"
        self.prepoznana.append(vsebina)
        return "novo spoznanje – vtis v zavest"

    def stanje(self) -> dict:
        return {"Prepoznana": self.prepoznana, "Ponovitve": self.ponovitve}


class AgentD:
    """Recognizes forms and types of đ-napetost within expressions."""

    def __init__(self):
        self.preboji = []
        self.pretoki = []

    def prepoznaj(self, izraz: str) -> str:
        lower = izraz.lower()
        if any(x in lower for x in ["udarec", "prelom", "žig", "eksces", "odmev", "rez"]):
            self.preboji.append(izraz)
            return "oblika đ – preboj ali singularna rana"
        if any(x in lower for x in ["tresljaj", "oscilacija", "pulz", "tok", "ritem", "glas"]):
            self.pretoki.append(izraz)
            return "vrsta đ – zvocno-poljski pretok"
        return "neklasificirana đ-napetost"

    def stanje(self) -> dict:
        return {"Oblike": self.preboji, "Vrste": self.pretoki}

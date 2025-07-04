class BodyAgent:
    """Agent representing the body's phases."""

    def __init__(self):
        self.state = "Material"

    def transition(self, symbol: str) -> str:
        if symbol == "Material":
            self.state = "Material"
            print("Telo: Material - Stik z zunanjim svetom, omejitve fizi\u010dnega sveta.")
        elif symbol == "Sensation":
            self.state = "Sensation"
            print("Telo: Sensation - Zaznavanje, fizi\u010dne ob\u010dutke.")
        elif symbol == "Action":
            self.state = "Action"
            print("Telo: Action - Fizi\u010dne reakcije in dejanja.")
        else:
            print("Neznan simbol za telo.")
        return self.state

    def get_state(self) -> str:
        return self.state


class SoulAgent:
    """Agent representing the soul's phases."""

    def __init__(self):
        self.state = "Awareness"

    def transition(self, symbol: str) -> str:
        if symbol == "Awareness":
            self.state = "Awareness"
            print("Du\u0161a: Awareness - Samozavedanje, refleksija.")
        elif symbol == "Emotion":
            self.state = "Emotion"
            print("Du\u0161a: Emotion - \u010custva, notranje izku\u0161nje.")
        elif symbol == "Reflection":
            self.state = "Reflection"
            print("Du\u0161a: Reflection - Razmi\u0161ljanje, iskanje smiselnosti.")
        else:
            print("Neznan simbol za du\u0161o.")
        return self.state

    def get_state(self) -> str:
        return self.state


class SpiritAgent:
    """Agent representing the spirit's phases."""

    def __init__(self):
        self.state = "Divine"

    def transition(self, symbol: str) -> str:
        if symbol == "Divine":
            self.state = "Divine"
            print("Duh: Divine - Povezava z bo\u017eanskim, neskon\u010dnost.")
        elif symbol == "Unity":
            self.state = "Unity"
            print("Duh: Unity - Enotnost, transcendenca.")
        elif symbol == "Eternal":
            self.state = "Eternal"
            print("Duh: Eternal - Nespremenljivost, ve\u010dno bivanje.")
        else:
            print("Neznan simbol za duh.")
        return self.state

    def get_state(self) -> str:
        return self.state

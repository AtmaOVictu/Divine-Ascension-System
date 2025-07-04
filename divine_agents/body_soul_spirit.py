class BodyAgent:
    """Represents the physical aspect of existence."""

    def __init__(self):
        self.state = "Material"

    def transition(self, symbol: str) -> None:
        if symbol == "Material":
            self.state = "Material"
            print("Telo: Material - Stik z zunanjim svetom, omejitve fizičnega sveta.")
        elif symbol == "Sensation":
            self.state = "Sensation"
            print("Telo: Sensation - Zaznavanje, fizične občutke.")
        elif symbol == "Action":
            self.state = "Action"
            print("Telo: Action - Fizične reakcije in dejanja.")
        else:
            print("Neznan simbol za telo.")

    def get_state(self) -> str:
        return self.state


class SoulAgent:
    """Represents the soul aspect mediating between body and spirit."""

    def __init__(self):
        self.state = "Awareness"

    def transition(self, symbol: str) -> None:
        if symbol == "Awareness":
            self.state = "Awareness"
            print("Duša: Awareness - Samozavedanje, refleksija.")
        elif symbol == "Emotion":
            self.state = "Emotion"
            print("Duša: Emotion - Čustva, notranje izkušnje.")
        elif symbol == "Reflection":
            self.state = "Reflection"
            print("Duša: Reflection - Razmišljanje, iskanje smiselnosti.")
        else:
            print("Neznan simbol za dušo.")

    def get_state(self) -> str:
        return self.state


class SpiritAgent:
    """Represents the spiritual aspect seeking transcendence."""

    def __init__(self):
        self.state = "Divine"

    def transition(self, symbol: str) -> None:
        if symbol == "Divine":
            self.state = "Divine"
            print("Duh: Divine - Povezava z božanskim, neskončnost.")
        elif symbol == "Unity":
            self.state = "Unity"
            print("Duh: Unity - Enotnost, transcendenca.")
        elif symbol == "Eternal":
            self.state = "Eternal"
            print("Duh: Eternal - Nespremenljivost, večno bivanje.")
        else:
            print("Neznan simbol za duh.")

    def get_state(self) -> str:
        return self.state

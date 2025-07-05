class Kapacitor:
    """Collects user inputs and triggers agent transitions."""

    def __init__(self):
        self.state = "Začetno"
        self.intensity = 0.0

    def process_answer(self, answer, agent):
        """Process user answer and update attached agent."""
        if answer == "aktiviraj":
            self.state = "Aktivacija"
            self.intensity += 0.3
            agent.update_emotion(0.6)
            new_state = agent.transition()
            return f"Sistem se aktivira! Agent je zdaj v stanju {new_state}."
        elif answer == "prehod":
            self.state = "Prehod"
            self.intensity += 0.5
            agent.update_emotion(0.8)
            new_state = agent.transition()
            return f"Prehod je uspešen, agent je zdaj v stanju {new_state}."
        elif answer == "zaključi":
            self.state = "Zaključek"
            self.intensity = 0
            agent.update_emotion(0)
            return "Proces je zaključen."
        return "Neznan ukaz."


class OkenskoSporocilo:
    """Simple interactive window representation."""

    def __init__(self, message="Dobrodošli!"):
        self.message = message

    def prompt(self):
        print(f"[INTERAKTIVNO OKNO] {self.message}")
        return input("Kako želite nadaljevati? (aktiviraj/prehod/zaključi): ")


class ModularnoOkno:
    """Allows dynamic extension with additional modules."""

    def __init__(self, name="Modularni sistem"):
        self.name = name

    def add_module(self, module):
        print(f"[MODUL] Dodajanje modula: {module}")
        if module == "Pomoč":
            print("Tukaj so navodila za pomoč...")
        elif module == "Povratne informacije":
            print("Vnesite povratne informacije o procesu.")

    def show(self):
        print(f"[OKNO] {self.name} je pripravljen na interakcijo.")
        choice = input("Izberite modul (Pomoč/Povratne informacije): ")
        self.add_module(choice)

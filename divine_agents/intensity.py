from dataclasses import dataclass


@dataclass
class Intensity:
    """Represents intensity levels with associated states and color codes."""

    state: str = "normalno"
    intensity: float = 0.0

    COLOR_MAP = {
        "visoka napetost": "Rdeča",
        "prehod": "Rumena",
        "stabilnost": "Zelena",
        "razjasnitev": "Modra",
        "negacija": "Črna",
    }

    def increase(self) -> str:
        """Increase intensity based on current state and return colored output."""
        if self.state == "visoka napetost":
            self.intensity += 0.8
        elif self.state == "prehod":
            self.intensity += 0.5
        elif self.state == "stabilnost":
            self.intensity += 0.2
        elif self.state == "razjasnitev":
            self.intensity += 0.3
        elif self.state == "negacija":
            self.intensity = 0

        color = self.COLOR_MAP.get(self.state, "Bela")
        message = f"Intenziteta je {self.intensity} in stanje je ozna\u010deno z barvo {color}."
        if self.intensity > 0.7:
            return message.upper()
        return message

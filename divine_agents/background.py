"""Utilities to generate random background stories for agents."""
import random

ORIGINS = [
    "majhnega mesteca",
    "velike prestolnice",
    "oddaljene vasice",
    "misticnega svetišča",
]

TRAITS = [
    "pogumen",
    "radoveden",
    "modrec",
    "neustavljiv popotnik",
]

PURPOSES = [
    "iskanje absolutne resnice",
    "raziskovanje relativnih pogledov",
    "zlitje vseh resnic v eno",
]

def generate_background(name: str) -> str:
    """Return a random background story for the given agent."""
    origin = random.choice(ORIGINS)
    trait = random.choice(TRAITS)
    purpose = random.choice(PURPOSES)
    return (
        f"{name} prihaja iz {origin}, poznan kot {trait}, "
        f"z namenom {purpose}."
    )

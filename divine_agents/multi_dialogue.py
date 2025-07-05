"""Napredna razprava med vec agenti v slovenščini."""

from typing import List

from .agent import Agent


def vecstranska_razprava(agenti: List[Agent]) -> List[str]:
    """Izvede razpravo med več agenti in posodobi njihova stanja."""
    vrstice = []
    # Začetni odgovori vsak agent izrazi svojo resnico
    for ag in agenti:
        vrstice.append(f"{ag.name} ({ag.state}): {ag.respond('Kaj je resnica?')}")

    # Vsak agent poveča čustva, kar lahko sproži prehode
    for ag in agenti:
        ag.update_emotion(0.6)
        novo_stanje = ag.transition()
        vrstice.append(f"{ag.name} prehaja v stanje: {novo_stanje}")

    # Ponovni odgovori po prehodih
    for ag in agenti:
        vrstice.append(f"{ag.name}: {ag.respond('Kaj je resnica?')}")

    return vrstice

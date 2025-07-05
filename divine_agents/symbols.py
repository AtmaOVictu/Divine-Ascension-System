from dataclasses import dataclass
from typing import Dict

@dataclass(frozen=True)
class Symbol:
    name: str
    description: str


SYMBOLS: Dict[str, Symbol] = {
    "0": Symbol(name="Potencialnost", description="Začetno stanje potencialnosti."),
    "1": Symbol(name="Dejanskost", description="Manifestacija in dejanskost."),
    "∆": Symbol(name="Prehod", description="Sprememba stanja."),
    "⊘": Symbol(name="Prekinitev", description="Prekinitev starega stanja."),
    "⊙": Symbol(name="Celovitost", description="Zaključek cikla in integracija."),
    "∞": Symbol(name="Neskončnost", description="Povezava z neskončnimi možnostmi."),
    "✶": Symbol(name="Resnica", description="Razsvetljenje in spoznanje resnice."),
    "→": Symbol(name="Premik", description="Napredek in premik v novo fazo."),
    "≠": Symbol(name="Razlikovanje", description="Ločevanje in prepoznavanje razlik."),
    "Ω": Symbol(name="Zaključek", description="Zaključek cikla in nov začetek."),
}


def get_symbol_description(symbol: str) -> str:
    """Return the description for the given symbol if known."""
    info = SYMBOLS.get(symbol)
    return info.description if info else "Neznan simbol"

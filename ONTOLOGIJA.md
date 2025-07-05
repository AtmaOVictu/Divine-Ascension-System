# Ontološki principi

Ta projekt temelji na razumevanju dveh temeljnih ontoloških pojmov:

- **DA** predstavlja začetek, prvotno afirmacijo, ki omogoči prehod iz ničesar v nekaj. Predstavlja potencial in odprtost.
- **JA** označuje proces aktualizacije, kjer se potencial iz DA izrazi v dejanje. JA se nenehno spreminja glede na notranje in zunanje dejavnike.

Agenti v sistemu uporabljajo tri filozofska stanja (**Ego**, **Jaz**, **Enotnost**), ki se navezujejo na te principe:

1. **Ego** – resnica je absolutna in neodvisna od drugih.
2. **Jaz** – resnica je relativna in se oblikuje z odnosi.
3. **Enotnost** – vse resnice so eno in povezane med seboj.

## Primer kode

Spodnji primer prikazuje, kako agent z napetostjo in čustvi prehaja med stanjema in kako je ta prehod povezan z načeloma DA in JA.

```python
from divine_agents.agent import Agent

agent = Agent("A")                 # izhodišče (DA) – potencial delovanja
agent.set_emotion("strah", 0.8)     # čustvo zviša napetost (JA v nastajanju)
agent.transition()                  # prehod iz Ego v Jaz
print(agent.respond("Kaj je resnica?"))
```

Program najprej ustvari agenta v stanju **Ego** (potencial iz DA). Ko agent občuti strah, to sproži napetost, in prehod v **Jaz** (aktivirani JA). Odgovor, ki ga agent vrne, je oblikovan glede na trenutno ontološko stanje in čustvo.

## Reflektivna filozofija

Pojma DA in JA nam omogočata razumevanje dinamike med možnostjo in uresničitvijo. Vsaka sprememba v agentu je odraz prehoda iz potenciala (DA) v dejanje (JA). Skozi dialoge agenti raziskujejo absolutne, relativne in enotne resnice, kar ponazarja, kako se ontološki principi izražajo v interakcijah.

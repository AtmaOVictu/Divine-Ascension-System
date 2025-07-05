# Ontološki principi

Ta datoteka ponuja kratek pregled ontoloških konceptov **JA** in **DA** ter njihovo povezavo s programskim modelom agentov.

## JA kot aktivacija

"JA" označuje potrditev ali dejanje, ki iz potenciala ustvari dejansko stanje. V kodi se to lahko ponazori s preprosto funkcijo:

```python
def JA_activation():
    status = "Aktiviran"
    return status
```

## DA kot možnost

"DA" predstavlja polje možnosti in relativnosti. Na ravni kode ga lahko opišemo takole:

```python
def DA_possibility():
    status = "Možnost"
    return status
```

## Prehod med fazami

Agenti v projektu `divine_agents` ponazarjajo prehod med filozofskimi fazami **Ego**, **Jaz** in **Enotnost**. Prehodi so sproženi z višjo napetostjo ali čustvi in odražajo logiko premika iz potenciala (DA) v aktivacijo (JA).

```python
from divine_agents.agent import Agent

agent = Agent("Filozof")
agent.update_tension(0.8)
agent.transition()  # prehod v stanje "Jaz"
```

V zgornjem primeru se napetost poveča nad prag, zato agent preide v naslednjo ontološko fazo.

## Refleksivna misel

Ontološke faze ponazarjajo razvoj razumevanja resnice:

- **Ego**: resnica je popolnoma absolutna.
- **Jaz**: resnica je relativna in se razkriva skozi odnose.
- **Enotnost**: vse resnice so eno in medsebojno povezane.

Agenti s svojimi prehodi raziskujejo to pot od abstraktne možnosti (DA) do polne aktivacije (JA), kar ponazarja večni cikel spoznavanja.


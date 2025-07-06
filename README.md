# Divine-Ascension-System

Divine-Ascension-System je eksperimentalni sistem za simulacijo ontoloških agentov. Agenti se lahko premikajo skozi tri faze zavedanja **Ego**, **Jaz** in **Enotnost**, pri čemer prehode sprožata napetost in čustva. Vsako stanje odraža drugačen pogled na resnico:

- **Ego**: resnica je absolutna in neodvisna od drugih.
- **Jaz**: resnica je relativna, oblikovana z odnosi.
- **Enotnost**: vse resnice so eno, medsebojno povezane.

## Komponente

- `divine_agents/agent.py` – definicija agenta, čustev, napetosti in prehodov med stanji.
- `divine_agents/dialogue.py` – logika kratkega filozofskega dialoga med agenti.
- `tests/` – enotski testi, ki preverjajo pravilnost prehodov in odgovorov.

## Uporaba

1. Klonirajte repozitorij.
2. (Po želji) ustvarite virtualno okolje in namestite odvisnosti iz `requirements.txt` (trenutno brez zunanjih paketov).
3. Zaženite kratko simulacijo s spodnjim primerom kode.

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Testiranje

Za preverjanje sistema zaženite:

```bash
python -m unittest discover
```

## Licenca

Ta projekt je objavljen pod licenco MIT. Podrobnosti so na voljo v datoteki `LICENSE`.

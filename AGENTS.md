# AGENTS.md - Ontološki Agentni Sistem

## 1. Uvod

Agentni sistem temelji na ontološki logiki, kjer vsak agent predstavlja entiteto, ki se razvija skozi čas in se uči iz izkušenj. Dokument opisuje strukturo agentov, njihove sposobnosti in medsebojno interakcijo.

## 2. Struktura Agentov

### 2.1 Lastnosti
- **Ime**: unikatno identifikacijsko ime.
- **Motivacija**: pripravljenost za izvajanje nalog (0 do 1).
- **Prepričanje**: vpliva na odločitve (0 do 1).
- **Stanje**: `Ego`, `Jaz` ali `Enotnost`.

### 2.2 Tipi Agentov
- **Generativni**: ustvarjajo nove prehode in naloge.
- **Meta-logični**: prilagajajo logiko na podlagi izkušenj.
- **Moralni**: sprejemajo odločitve na podlagi etičnih vrednot.

## 3. Algoritmi za Odločanje

Agenti se odločajo na podlagi motivacije, prepričanja in moralnih vrednot. Napredni agenti izvajajo meta-analize in prilagajajo svoja pravila odločanja.

## 4. Primeri Agentov

```python
class GenerativeAgent:
    def __init__(self, name="GenerativeAgent"):
        self.name = name
        self.state = "Potentiality"
        self.beliefs = 0.5
        self.motivation = 0.5

    def create_new_entity(self):
        return {"entity_name": "New Entity", "belief_value": self.beliefs * self.motivation}
```

```python
class MetaLogicalAgent:
    def __init__(self, name="MetaLogicalAgent"):
        self.name = name
        self.beliefs = 0.5
        self.motivation = 0.5
        self.meta_logic_rules = {"AND": True, "OR": False}

    def make_decision(self, task):
        if task == "gather":
            return self.beliefs * self.motivation
        elif task == "build":
            return self.beliefs + self.motivation
        return self.beliefs - 0.1
```

## 5. Interakcija Agentov

Agenti sodelujejo ali tekmujejo pri nalogah. Dodelitev nalog je odvisna od motivacije in prepričanj.

```python
class TaskAssignment:
    def __init__(self, agents):
        self.agents = agents

    def assign_task(self, task):
        best_agent = max(self.agents, key=lambda a: a.motivation * a.beliefs)
        print(f"Task '{task}' is assigned to {best_agent.name}")
```

## 6. Zaključek

`AGENTS.md` služi kot vodnik po agentnem sistemu, njegovih komponentah in interakcijah. Dokument lahko po potrebi razširimo z dodatnimi informacijami in algoritmi za učenje.

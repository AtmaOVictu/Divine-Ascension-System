# Ontological Principles

This project explores agent-based interactions grounded in three primary states:

- **Ego (⊘)** – truth is **absolute** and independent of others.
- **Jaz (∫(dru/x))** – truth is **relative**, formed by relationships.
- **Enotnost (RES001)** – truth is **unified**; all truths are one.

Agents transition between states when *tension* exceeds `0.7` or *emotion* intensity is above `0.5`. Each emotion also has a type (joy, anger, fear) that colors the agent's responses.

## Ontological Flow with JA and DA

JA marks the moment when possibility becomes actual. DA signals the field of potential. Within this framework:

```python
agent = Agent("A")
print(agent.respond("Kaj je resnica?"))
# => "Resnica je absolutna in neodvisna od drugih."

agent.set_emotion("strah", 0.6)
agent.transition()  # moves to "Jaz" because emotion > 0.5
print(agent.respond("Kaj je resnica?"))
# => "Resnica je relativna, oblikovana z našimi odnosi. (čutim strah)"
```

Here, the act of calling `transition()` is analogous to moving from DA (potential) to JA (realization). By raising tension or emotion, the agent embodies the decision to move beyond its current view of truth.

## Reflective Philosophy

1. **Ego** anchors certainty: "I alone define truth." This reflects a stable JA.
2. **Jaz** acknowledges interplay: "Truth emerges through us." The agent recognizes DA as possibility shaped by others.
3. **Enotnost** unites all perspectives: "Every truth converges." Here, JA and DA intertwine as one.

These transitions invite reflection on how emotions guide philosophical growth. Fear might push an Ego-driven agent to question absolutes, while joy could open a Jaz agent toward unity.


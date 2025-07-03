# Divine-Ascension-System

This project simulates interactions between ontological agents transitioning
through different philosophical states: **Ego**, **Jaz** and **Enotnost**.
Agents hold internal emotion and tension values which influence state
transitions and dialogue.

## Agent States
- **Ego**: Truth is absolute and independent of others.
- **Jaz**: Truth is relative, shaped by relationships.
- **Enotnost**: All truths are one and interconnected.

State transitions occur when an agent's tension exceeds `0.7` or its emotion
intensity exceeds `0.5`.

## Emotional Responses
`Agent.respond(question, emotion)` returns a philosophical statement based on
the agent's state and emotional context (`fear`, `joy` or `anger`). The table
below summarises how emotions modify responses:

| State     | Fear                                                            | Joy                                                         | Anger                                                         |
|-----------|-----------------------------------------------------------------|-------------------------------------------------------------|---------------------------------------------------------------|
| **Ego**   | "Čutim strah, a verjamem, da je resnica še vedno absolutna."   | "Z veseljem zagovarjam absoluten pogled na resnico."        | "Z jezo branim svoje prepričanje o absolutni resnici."        |
| **Jaz**   | "Čeprav me je strah, razumem, da je resnica relativna."        | "Z veseljem priznavam relativnost resnice."                 | "Z jezo opozarjam, da se resnica oblikuje skozi odnose."      |
| **Enotnost** | "Četudi obstaja strah, spoznavam, da so vse resnice ena."   | "Z radostjo sprejemam, da so vse resnice medsebojno povezane." | "Tudi v jezi vidim, da je vse povezano v enotni resnici."  |

## Dialogue
`philosophical_dialogue(agent1, agent2)` demonstrates a short conversation in
which agents reply according to their state and emotion. Initial answers use
`fear` and `anger` to showcase differing perspectives. After updating emotional
intensity, agents transition states when thresholds are met and respond again
with `joy`.

Unit tests located in `tests/` verify transitions, emotional responses and
sample dialogues.

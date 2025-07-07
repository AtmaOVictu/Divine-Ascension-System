# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Emotion Levels

Agent responses change depending on the current emotion value:

- **Low (\<= 0.4)** – returns the base philosophical statement.
- **Medium (\> 0.4 and \<= 0.7)** – appends "Rahlo čustveno pojasnjujem." to the base text.
- **High (\> 0.7)** – appends "Z veliko strastjo razlagam." for a passionate tone.

These additions are produced by the `Agent.respond` method.

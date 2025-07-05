class Symbol:
    """A simple symbolic representation supporting non-ASCII names."""

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Symbol('{self.name}')"


class Expression:
    """Basic symbolic expression container."""

    def __init__(self, *terms):
        self.terms = list(terms)

    def __str__(self) -> str:
        return " + ".join(str(t) for t in self.terms)

    def __repr__(self) -> str:
        return f"Expression({', '.join(repr(t) for t in self.terms)})"

    def integrate(self, var: Symbol) -> 'Expression':
        """Return a placeholder integral expression."""
        return Expression(f"∫({self}) d{var}")

    def differentiate(self, var: Symbol) -> 'Expression':
        """Return a placeholder derivative expression."""
        return Expression(f"d({self})/d{var}")

    def simplify(self) -> 'Expression':
        """Return a simplified form (identity for now)."""
        return self

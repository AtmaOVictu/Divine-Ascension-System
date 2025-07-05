class Symbolic:
    """Minimal symbolic expression class for demonstration."""

    def __init__(self, expr):
        self.expr = str(expr)

    def __str__(self):
        return self.expr

    __repr__ = __str__

    def _wrap(self, other):
        if isinstance(other, Symbolic):
            return other.expr
        return str(other)

    def __add__(self, other):
        return Symbolic(f"({self.expr}) + ({self._wrap(other)})")

    def __sub__(self, other):
        return Symbolic(f"({self.expr}) - ({self._wrap(other)})")

    def __mul__(self, other):
        return Symbolic(f"({self.expr}) * ({self._wrap(other)})")

    def __pow__(self, power):
        return Symbolic(f"({self.expr})**{self._wrap(power)}")

    def simplify(self):
        return self

    def integrate(self, var):
        var_str = self._wrap(var)
        return Symbolic(f"integral({self.expr}, {var_str})")

    def diff(self, var):
        var_str = self._wrap(var)
        return Symbolic(f"diff({self.expr}, {var_str})")


def sin(arg):
    return Symbolic(f"sin({arg})")

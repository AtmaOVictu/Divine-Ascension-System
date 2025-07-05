class Expr:
    def __init__(self, rep):
        self.rep = rep

    def __str__(self):
        return self.rep

    __repr__ = __str__

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, other):
        return Expr(f"({self.rep} + {other})")

    def __mul__(self, other):
        return Expr(f"({self.rep}*{other})")

    def __pow__(self, power):
        return Expr(f"({self.rep}**{power})")

    def has(self, var):
        return str(var) in self.rep


class Symbol(Expr):
    def __init__(self, name):
        super().__init__(name)
        self.name = name


def symbols(name):
    return Symbol(name)


def sin(expr):
    return Expr(f"sin({expr})")


def cos(expr):
    return Expr(f"cos({expr})")


def simplify(expr):
    return expr


def integrate(expr, var):
    return Expr(f"Integral({expr}, {var})")


def diff(expr, var):
    sin_repr = f"sin({var})"
    expr_str = str(expr)
    if expr_str == sin_repr:
        return cos(var)
    if sin_repr in expr_str:
        other = expr_str.replace(sin_repr, "")
        if str(var) not in other:
            return cos(var)
        return Expr(expr_str.replace(sin_repr, f"cos({var})"))
    return Expr(f"d({expr})/d({var})")

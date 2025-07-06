"""Utility functions for mathematical expression evaluation and simple music generation."""

from typing import List
import math
import operator
import ast

_ALLOWED_NAMES = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
_ALLOWED_NAMES.update({"abs": abs, "round": round})


class _SafeEvaluator(ast.NodeVisitor):
    """Safely evaluate mathematical expressions using AST."""

    def __init__(self, expr: str):
        self.expr = expr

    def visit(self, node):
        if isinstance(node, ast.Expression):
            return self.visit(node.body)
        elif isinstance(node, ast.BinOp):
            left = self.visit(node.left)
            right = self.visit(node.right)
            return self._binop(node.op)(left, right)
        elif isinstance(node, ast.UnaryOp):
            operand = self.visit(node.operand)
            return self._unaryop(node.op)(operand)
        elif isinstance(node, ast.Num):  # type: ignore[deprecated-name]
            return node.n
        elif isinstance(node, ast.Name):
            if node.id not in _ALLOWED_NAMES:
                raise ValueError(f"Use of '{node.id}' is not allowed")
            return _ALLOWED_NAMES[node.id]
        elif isinstance(node, ast.Call):
            func = self.visit(node.func)
            args = [self.visit(a) for a in node.args]
            return func(*args)
        else:
            raise ValueError(f"Unsupported expression: {ast.dump(node)}")

    def _binop(self, op):
        operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.Mod: operator.mod,
        }
        return operators[type(op)]

    def _unaryop(self, op):
        operators = {ast.UAdd: operator.pos, ast.USub: operator.neg}
        return operators[type(op)]


def evaluate_equation(expr: str) -> float:
    """Evaluate a math expression securely."""
    tree = ast.parse(expr, mode="eval")
    evaluator = _SafeEvaluator(expr)
    return evaluator.visit(tree)


_NOTES_ORDER = ["C", "D", "E", "F", "G", "A", "B"]


def generate_major_scale(key: str) -> List[str]:
    """Generate a simple major scale for the given key."""
    if key not in _NOTES_ORDER:
        raise ValueError("Key must be one of " + ", ".join(_NOTES_ORDER))
    start = _NOTES_ORDER.index(key)
    scale = [_NOTES_ORDER[(start + i) % len(_NOTES_ORDER)] for i in range(7)]
    return scale

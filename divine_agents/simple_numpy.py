"""Minimal numpy-like utilities for environments without numpy."""
import random


def rand(*shape):
    if len(shape) == 1:
        return [random.random() for _ in range(shape[0])]
    elif len(shape) == 2:
        return [[random.random() for _ in range(shape[1])] for _ in range(shape[0])]
    raise ValueError("Only 1D or 2D shapes supported")


def zeros(shape):
    if isinstance(shape, tuple):
        rows, cols = shape
        return [[0.0 for _ in range(cols)] for _ in range(rows)]
    return [0.0 for _ in range(shape)]


def dot(a, b):
    if isinstance(a[0], list):
        # matrix multiplication
        result = []
        if isinstance(b[0], list):
            for row in a:
                new_row = []
                for col in zip(*b):
                    new_row.append(sum(x*y for x, y in zip(row, col)))
                result.append(new_row)
        else:
            for row in a:
                result.append(sum(x*y for x, y in zip(row, b)))
        return result
    else:
        # vector dot product
        return sum(x*y for x, y in zip(a, b))


def clip(values, low, high):
    if isinstance(values, list):
        return [max(low, min(high, v)) for v in values]
    return max(low, min(high, values))


def mean(matrix):
    total = 0.0
    count = 0
    if isinstance(matrix[0], list):
        for row in matrix:
            total += sum(row)
            count += len(row)
    else:
        total = sum(matrix)
        count = len(matrix)
    return total / count


def array(lst):
    # trivial passthrough
    return [row[:] if isinstance(row, list) else row for row in lst]

import random

import random as _r

class _Random:
    @staticmethod
    def rand(*shape):
        if len(shape) == 1:
            return [_r.random() for _ in range(shape[0])]
        elif len(shape) == 2:
            return [[_r.random() for _ in range(shape[1])] for _ in range(shape[0])]
        else:
            raise NotImplementedError

random = _Random()


def zeros(n):
    return [0.0 for _ in range(n)]


def array(seq):
    if isinstance(seq, list):
        return seq.copy()
    return list(seq)


def dot(a, b):
    if isinstance(a[0], list):
        rows_a = len(a)
        cols_a = len(a[0])
        cols_b = len(b[0])
        result = [[0.0 for _ in range(cols_b)] for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                s = 0.0
                for k in range(cols_a):
                    s += a[i][k] * b[k][j]
                result[i][j] = s
        return result
    else:
        return sum(x * y for x, y in zip(a, b))


def clip(arr, a_min, a_max):
    if isinstance(arr, list):
        return [max(a_min, min(a_max, x)) for x in arr]
    return max(a_min, min(a_max, arr))


def mean(matrix):
    total = sum(sum(row) for row in matrix)
    count = len(matrix) * len(matrix[0])
    return total / count

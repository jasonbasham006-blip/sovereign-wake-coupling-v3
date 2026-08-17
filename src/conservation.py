"""
Structural conservation and matrix integrity checks.

These gates test algebraic consistency of the reduced model.
They do not constitute a derivation of physical energy or angular-momentum
exchange with the wake medium; that remains an open theoretical layer.
"""

from __future__ import annotations
from typing import List


def check_zero_diagonal(W: List[List[float]], tol: float = 1e-30) -> bool:
    """Diagonal elements of the mutual matrix must vanish."""
    n = len(W)
    for i in range(n):
        if abs(W[i][i]) > tol:
            return False
    return True


def linear_momentum_residual(forces: List[float], tol: float = 1e-6) -> float:
    """
    For an isolated pairwise system the sum of forces should vanish
    (action-reaction). Returns the absolute residual.
    """
    return abs(sum(forces))


def antisymmetry_score(W: List[List[float]]) -> float:
    """
    Measure of departure from antisymmetry in a force-proxy matrix.
    Returns max |W_ij + W_ji| over off-diagonal pairs (0 = perfect).
    Note: the reduced geometric form used here is not required to be
    antisymmetric; this metric is diagnostic only.
    """
    n = len(W)
    max_dev = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            dev = abs(W[i][j] + W[j][i])
            if dev > max_dev:
                max_dev = dev
    return max_dev

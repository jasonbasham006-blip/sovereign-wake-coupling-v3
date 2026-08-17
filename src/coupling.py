"""
Mutual wake coupling matrix construction.

The algebraic form used here is a reduced-order, quasi-static approximation.
A full Green-function derivation from the field equation is the intended
next theoretical layer; this module keeps the structure explicit and testable.
"""

from __future__ import annotations
import math
from typing import List

from .bodies import CelestialBody
from .constants import DM_DENSITY


def compute_source_current(body: CelestialBody, rho_dm: float = DM_DENSITY) -> float:
    """
    Phenomenological source intensity:
        J ~ m_total * rho_dm * (C_d * v^2)

    This is labeled phenomenological until derived from an explicit
    matter-field interaction Lagrangian.
    """
    return body.mass_total * rho_dm * (body.cd_phase * (body.velocity ** 2))


def build_mutual_wake_matrix(bodies: List[CelestialBody],
                             rho_dm: float = DM_DENSITY) -> List[List[float]]:
    """
    Construct N x N coupling matrix W[i][j].

    W_ij = source_i * geometric_kernel * cross_section_j
    Diagonal is identically zero (no self-wake in this reduced model).
    """
    n = len(bodies)
    W = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            bi = bodies[i]
            bj = bodies[j]
            dist = abs(bi.distance - bj.distance)
            if dist < 1.0:          # hard floor to avoid singularity
                dist = max(bj.distance, bi.distance, 1.0) + 1.0
            source = compute_source_current(bi, rho_dm)
            kernel = 1.0 / (4.0 * math.pi * (dist ** 2))
            W[i][j] = source * kernel * bj.cross_section
    return W

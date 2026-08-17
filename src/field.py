"""
Wake-field Lagrangian layer.

Provides the explicit field structure that underpins conservation bookkeeping.
The source functional J remains phenomenological until derived from a concrete
matter-field interaction.
"""

from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Callable, Optional

from .constants import C_PHI_DEFAULT, M_PHI_DEFAULT


@dataclass
class WakeFieldLagrangian:
    """
    Minimal scalar-field Lagrangian density (flat space):

        L = 1/2 * phidot^2 - 1/2 * c_phi^2 * |grad phi|^2 - V(phi) + J * phi

    Variation yields the driven Klein-Gordon equation.
    """
    c_phi: float = C_PHI_DEFAULT
    m_phi: float = M_PHI_DEFAULT
    potential: Optional[Callable[[float], float]] = None

    def V(self, phi: float) -> float:
        if self.potential is not None:
            return self.potential(phi)
        return 0.5 * (self.m_phi ** 2) * (phi ** 2)

    def dV_dphi(self, phi: float) -> float:
        # Quadratic default
        return (self.m_phi ** 2) * phi

    def field_equation_rhs(self, phi: float, J: float) -> float:
        """
        Right-hand side of:
            d²phi/dt² - c² ∇²phi + V'(phi) = J
        (spatial Laplacian handled by the Green-function / solver layer)
        """
        return J - self.dV_dphi(phi)


def dispersion_relation(k: float, c_phi: float = C_PHI_DEFAULT, m_phi: float = M_PHI_DEFAULT) -> float:
    """
    omega^2 = c_phi^2 * k^2 + m_phi^2
    Returns angular frequency omega (rad/s) for wave-number k (1/m).
    """
    return math.sqrt((c_phi * k) ** 2 + m_phi ** 2)


def energy_density(phi: float, phidot: float, grad_phi_sq: float,
                   c_phi: float = C_PHI_DEFAULT, m_phi: float = M_PHI_DEFAULT,
                   J: float = 0.0) -> float:
    """
    Field energy density (source-free piece + interaction):
        T00 ~ 1/2 phidot^2 + 1/2 c^2 |grad phi|^2 + V - J phi
    """
    V = 0.5 * (m_phi ** 2) * (phi ** 2)
    return 0.5 * phidot**2 + 0.5 * c_phi**2 * grad_phi_sq + V - J * phi

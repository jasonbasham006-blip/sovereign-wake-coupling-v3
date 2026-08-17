"""Celestial body definitions and Solar-System initialization."""

from __future__ import annotations
import math
from dataclasses import dataclass, field
from typing import List

from .constants import SOLAR_EPSILON, AU


@dataclass
class CelestialBody:
    name: str
    mass_bary: float          # kg
    radius: float             # m
    distance_au: float        # AU
    velocity_km_s: float      # km/s
    cd_phase: float           # dimensionless composition / phase factor
    rotation_period_s: float  # s (negative for retrograde)

    # Derived / runtime fields
    mass_total: float = field(init=False)
    cross_section: float = field(init=False)
    distance: float = field(init=False)       # m
    velocity: float = field(init=False)       # m/s
    spin_omega: float = field(init=False)     # rad/s
    predicted_torque: float = field(default=0.0, init=False)

    def __post_init__(self) -> None:
        self.mass_total = self.mass_bary * (1.0 + SOLAR_EPSILON)
        self.cross_section = math.pi * (self.radius ** 2)
        self.distance = self.distance_au * AU
        self.velocity = self.velocity_km_s * 1000.0
        if self.rotation_period_s != 0.0:
            self.spin_omega = 2.0 * math.pi / abs(self.rotation_period_s)
            if self.rotation_period_s < 0:
                self.spin_omega = -self.spin_omega
        else:
            self.spin_omega = 0.0


def initialize_solar_system() -> List[CelestialBody]:
    """
    Nine-body benchmark architecture.
    Parameters are standard reference values; Cd phases are phenomenological.
    """
    return [
        CelestialBody("Sun",     1.98847e30, 6.9634e8,   0.0,    0.0,   2.5,  2.447e6),
        CelestialBody("Mercury", 3.3011e23,  2.4397e6,   0.387,  47.36, 1.0,  5.865e6),
        CelestialBody("Venus",   4.8675e24,  6.0518e6,   0.723,  35.02, 1.2, -2.099e7),
        CelestialBody("Earth",   5.9722e24,  6.371e6,    1.000,  29.78, 1.1,  86164.0),
        CelestialBody("Mars",    6.4171e23,  3.3895e6,   1.524,  24.07, 1.0,  88642.0),
        CelestialBody("Jupiter", 1.8982e27,  6.9911e7,   5.204,  13.07, 2.0,  35730.0),
        CelestialBody("Saturn",  5.6834e26,  5.8232e7,   9.582,  9.69,  1.9,  39240.0),
        CelestialBody("Uranus",  8.6810e25,  2.5362e7,  19.20,   6.81,  1.6,  62133.0),
        CelestialBody("Neptune", 1.0241e26,  2.4622e7,  30.05,   5.43,  1.6,  57996.0),
    ]

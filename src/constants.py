"""Physical and model constants for the wake-coupling framework."""

import math

# --- Fundamental / reference constants ---
G = 6.67430e-11                  # m^3 kg^-1 s^-2
AU = 1.495978707e11              # m
SOLAR_MASS = 1.98847e30          # kg
SOLAR_RADIUS = 6.9634e8          # m

# --- Model baseline parameters (phenomenological) ---
# Local galactic dark-matter density estimate (kg/m^3)
DM_DENSITY = 7.05e-27

# Age scaling used only for the optional mass-inflation factor
SOLAR_SYSTEM_AGE_GYR = 4.5
REFERENCE_AGE_GYR = 10.0
BH_BENCHMARK_EPSILON = 0.8689
SOLAR_EPSILON = BH_BENCHMARK_EPSILON * (SOLAR_SYSTEM_AGE_GYR / REFERENCE_AGE_GYR)

# --- Calibration target (Uranus) ---
# This is a fixed numerical target used solely for locking the global amplitude A.
# It is NOT an independent validation measurement inside this package.
URANUS_TARGET_TORQUE = 4.75584e18   # N·m

# --- Field parameters (phenomenological defaults) ---
# Propagation speed is constrained, not derived.
# Default set near the geometric Jupiter bound for demonstration only.
C_PHI_DEFAULT = 195.0               # m/s
M_PHI_DEFAULT = 0.0                 # mass term (s^-1 equivalent units in naturalized form)

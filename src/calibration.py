"""
Global amplitude calibration and out-of-sample torque prediction.

Protocol:
  1. Lock a single scalar A so that the model matches a chosen target torque
     on one body (Uranus by default).
  2. Apply the identical A to every other body without further tuning.
  3. Report those values as predictions, not validations.
"""

from __future__ import annotations
from typing import List, Tuple

from .bodies import CelestialBody
from .constants import URANUS_TARGET_TORQUE
from .coupling import build_mutual_wake_matrix


def calibrate_global_amplitude(bodies: List[CelestialBody],
                               target_body_name: str = "Uranus",
                               target_torque: float = URANUS_TARGET_TORQUE
                               ) -> Tuple[float, List[List[float]]]:
    """
    Returns (A, W) where A is the global amplitude that locks the named body
    to the supplied target torque.
    """
    W = build_mutual_wake_matrix(bodies)
    names = [b.name for b in bodies]
    if target_body_name not in names:
        raise ValueError(f"Target body '{target_body_name}' not found.")
    idx = names.index(target_body_name)
    net_coupling = sum(W[i][idx] for i in range(len(bodies)))
    lever = bodies[idx].radius
    if abs(net_coupling * lever) < 1e-40:
        raise RuntimeError("Degenerate coupling; cannot calibrate A.")
    A = target_torque / (net_coupling * lever)
    return A, W


def predict_torques(bodies: List[CelestialBody],
                    A: float,
                    W: List[List[float]]) -> List[float]:
    """
    Apply locked amplitude A to every body.
    Returns list of predicted torques (N·m) in the same order as bodies.
    """
    torques = []
    n = len(bodies)
    for j in range(n):
        net = sum(W[i][j] for i in range(n))
        tau = A * net * bodies[j].radius
        bodies[j].predicted_torque = tau
        torques.append(tau)
    return torques

"""Structural integrity tests for the wake-coupling package."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.bodies import initialize_solar_system
from src.coupling import build_mutual_wake_matrix
from src.calibration import calibrate_global_amplitude, predict_torques
from src.conservation import check_zero_diagonal
from src.constants import URANUS_TARGET_TORQUE
from src.field import dispersion_relation


def test_nine_bodies():
    bodies = initialize_solar_system()
    assert len(bodies) == 9


def test_zero_diagonal():
    bodies = initialize_solar_system()
    W = build_mutual_wake_matrix(bodies)
    assert check_zero_diagonal(W)


def test_uranus_calibration_locks():
    bodies = initialize_solar_system()
    A, W = calibrate_global_amplitude(bodies)
    torques = predict_torques(bodies, A, W)
    names = [b.name for b in bodies]
    idx = names.index("Uranus")
    assert abs(torques[idx] - URANUS_TARGET_TORQUE) / URANUS_TARGET_TORQUE < 1e-10


def test_finite_predictions():
    bodies = initialize_solar_system()
    A, W = calibrate_global_amplitude(bodies)
    torques = predict_torques(bodies, A, W)
    assert all(abs(t) < 1e40 for t in torques)
    assert all(t == t for t in torques)  # no NaNs


def test_dispersion_positive():
    omega = dispersion_relation(1e-8)
    assert omega > 0.0

"""
Demonstration runner for SOVEREIGN Wake Coupling v3.0

Executes the nine-body matrix construction, Uranus calibration,
and out-of-sample torque table. Prints an epistemic-status summary.
"""

from __future__ import annotations
import sys
from pathlib import Path

# Allow running as module or script
if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.bodies import initialize_solar_system
from src.calibration import calibrate_global_amplitude, predict_torques
from src.conservation import check_zero_diagonal
from src.constants import URANUS_TARGET_TORQUE, C_PHI_DEFAULT
from src.field import dispersion_relation


def main() -> None:
    print("=" * 66)
    print("  SOVEREIGN WAKE COUPLING RESEARCH  v3.0")
    print("  First-Principles Field-Theoretic N-Body Framework")
    print("=" * 66)
    print()

    bodies = initialize_solar_system()
    A, W = calibrate_global_amplitude(bodies)
    torques = predict_torques(bodies, A, W)

    print("[*] Calibration")
    print(f"    Global amplitude A ........ {A:.10e}")
    print(f"    Uranus target torque ...... {URANUS_TARGET_TORQUE:.5e} N·m")
    print(f"    Zero-diagonal check ....... {'PASS' if check_zero_diagonal(W) else 'FAIL'}")
    print()

    print("-" * 66)
    print(f"{'Body':<10} {'Predicted Torque (N·m)':>24}  {'Role':<22}")
    print("-" * 66)
    for body, tau in zip(bodies, torques):
        role = "CALIBRATION LOCK" if body.name == "Uranus" else "OUT-OF-SAMPLE"
        print(f"{body.name:<10} {tau:>24.4e}  {role:<22}")
    print("-" * 66)
    print()

    # Simple dispersion check at a representative wave-number
    k_demo = 1.0 / 1e8          # 1/(100 000 km)
    omega = dispersion_relation(k_demo, c_phi=C_PHI_DEFAULT)
    print("[*] Field layer (illustrative)")
    print(f"    c_phi (default) ........... {C_PHI_DEFAULT:.1f} m/s")
    print(f"    omega(k=1e-8 m^-1) ........ {omega:.6e} rad/s")
    print()

    print("[*] Epistemic gates")
    print("    Field Lagrangian structure ...... DERIVED")
    print("    Dispersion relation ............. DERIVED")
    print("    Source functional J ............. PHENOMENOLOGICAL")
    print("    Global amplitude A .............. CALIBRATED (Uranus)")
    print("    Other-body torques .............. PREDICTIONS ONLY")
    print("    Physical validation ............. NOT CLAIMED")
    print()
    print("=" * 66)
    print("  End of demonstration run.  See docs/EPISTEMIC_STATUS.md")
    print("=" * 66)


if __name__ == "__main__":
    main()

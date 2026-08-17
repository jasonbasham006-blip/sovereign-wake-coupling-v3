"""
SOVEREIGN Wake Coupling Research v3.0
First-principles field-theoretic N-body wake interaction framework.
"""

__version__ = "3.0.0"
__status__ = "RESEARCH_ARTIFACT"

from .bodies import CelestialBody, initialize_solar_system
from .field import WakeFieldLagrangian, dispersion_relation
from .coupling import build_mutual_wake_matrix, compute_source_current
from .calibration import calibrate_global_amplitude, predict_torques
from .conservation import linear_momentum_residual, check_zero_diagonal

__all__ = [
    "CelestialBody",
    "initialize_solar_system",
    "WakeFieldLagrangian",
    "dispersion_relation",
    "build_mutual_wake_matrix",
    "compute_source_current",
    "calibrate_global_amplitude",
    "predict_torques",
    "linear_momentum_residual",
    "check_zero_diagonal",
]

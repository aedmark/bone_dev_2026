"""
phases/__init__.py
Re-exports the phase classes so that external modules (like cycle.py)
can import from 'phases' exactly as they did when it was a single file.
"""

from .base import SimulationPhase
from .biological import MetabolismPhase, SensationPhase, IntrusionPhase
from .cognitive import CognitionPhase, ArbitrationPhase, SoulPhase, SimulationPreflightPhase
from .environmental import NavigationPhase, RealityFilterPhase, ObservationPhase, SanctuaryPhase
from .mechanical import MachineryPhase, MaintenancePhase, GatekeeperPhase, StabilizationPhase

__all__ = [
    "SimulationPhase",
    "ObservationPhase",
    "SanctuaryPhase",
    "MaintenancePhase",
    "GatekeeperPhase",
    "MetabolismPhase",
    "RealityFilterPhase",
    "NavigationPhase",
    "MachineryPhase",
    "IntrusionPhase",
    "SoulPhase",
    "ArbitrationPhase",
    "SimulationPreflightPhase",
    "CognitionPhase",
    "SensationPhase",
    "StabilizationPhase"
]
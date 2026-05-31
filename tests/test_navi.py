"""
tests/test_navi.py

Structural tensegrity tests for the CDGovernor (Creative Determinant) injection.
Ensures the Picard PDE solver resolves viability thresholds correctly, and
that the legacy PID loop engages if the vector field goes dark.
"""

import pytest
import numpy as np
from core import CyberneticGovernor, CD_AVAILABLE

def test_navi_installation_verified():
    """
    If this fails, the environment cannot see Nelson's library.
    The engine will survive, but it will be driving blind.
    """
    assert CD_AVAILABLE is True, "navi-creative-determinant is not accessible to the Python path."

@pytest.fixture
def governor():
    return CyberneticGovernor()

def test_pde_active_regulation(governor):
    """
    Test the PDE solving a nontrivial conversation state.
    """
    physics_state = {"voltage": 40.0, "narrative_drag": 1.0}
    goal_vec = np.array([1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], dtype=np.float32)
    dv, dd = governor.regulate(physics=physics_state, dt=1.0, goal_vector=goal_vec)
    assert isinstance(dv, float)
    assert isinstance(dd, float)
    assert governor.last_lam1 != 0.0
    assert governor.last_sol in ['trivial', 'nontrivial']

def test_pid_fallback(governor):
    """
    Test the legacy seatbelt. If the goal vector is None, we must gracefully
    fall back to a static PID loop without crashing the cycle.
    """
    governor.recalibrate(target_voltage=30.0, target_drag=0.6)
    physics_state = {"voltage": 20.0, "narrative_drag": 0.2}
    dv, dd = governor.regulate(physics=physics_state, dt=1.0, goal_vector=None)
    assert dv > 0.0, "PID failed to correct low voltage."
    assert dd > 0.0, "PID failed to correct low narrative drag."

def test_policy_shift_coregulation(governor):
    """
    A negative eigenvalue indicates emergent systemic tension.
    The macro-policy must shift to CO_REGULATION to sustain the loop.
    """
    governor.last_lam1 = -0.5
    governor.last_sol = 'nontrivial'
    assert governor.get_policy_shift() == 'CO_REGULATION'

def test_policy_shift_efficiency(governor):
    """
    A positive eigenvalue indicates mathematical boredom/dissolution.
    The macro-policy must shift to EFFICIENCY to wrap up the transaction.
    """
    governor.last_lam1 = 1.2
    governor.last_sol = 'trivial'
    assert governor.get_policy_shift() == 'EFFICIENCY'

def test_endocrine_stress_modifier(governor):
    """
    Validates that the biological substrate still correctly throttles
    the mathematical time-delta during regulation.
    """
    class MockEndo:
        glimmers = 2
    physics_state = {"voltage": 30.0, "narrative_drag": 0.6}
    goal_vec = np.array([0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], dtype=np.float32)
    dv1, dd1 = governor.regulate(physics_state, dt=1.0, goal_vector=goal_vec, endocrine_state=None)
    dv2, dd2 = governor.regulate(physics_state, dt=1.0, goal_vector=goal_vec, endocrine_state=MockEndo())
    assert abs(dv2) >= abs(dv1)
    assert abs(dd2) >= abs(dd1)
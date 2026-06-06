""" tests/test_navi.py """

import pytest
import numpy as np
from core import CyberneticGovernor

@pytest.fixture
def governor():
    return CyberneticGovernor()

def test_pde_active_regulation(governor):
    physics_state = {"voltage": 40.0, "narrative_drag": 1.0}
    goal_vec = np.array([1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], dtype=np.float32)
    dv, dd = governor.regulate(physics=physics_state, dt=1.0, goal_vector=goal_vec)
    assert isinstance(dv, float)
    assert isinstance(dd, float)
    assert governor.last_lam1 != 0.0
    assert governor.last_sol in ['trivial', 'nontrivial']

def test_pid_fallback(governor):
    governor.recalibrate(target_voltage=30.0, target_drag=0.6)
    physics_state = {"voltage": 20.0, "narrative_drag": 0.2}
    dv, dd = governor.regulate(physics=physics_state, dt=1.0, goal_vector=None)
    assert dv > 0.0, "PID failed to correct low voltage."
    assert dd > 0.0, "PID failed to correct low narrative drag."

def test_policy_shift_coregulation(governor):
    governor.last_lam1 = -0.5
    governor.last_sol = 'nontrivial'
    assert governor.get_policy_shift() == 'CO_REGULATION'

def test_policy_shift_efficiency(governor):
    governor.last_lam1 = 1.2
    governor.last_sol = 'trivial'
    assert governor.get_policy_shift() == 'EFFICIENCY'

def test_endocrine_stress_modifier(governor):
    class MockEndo:
        glimmers = 2
    physics_state = {"voltage": 30.0, "narrative_drag": 0.6}
    goal_vec = np.array([0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], dtype=np.float32)
    dv1, dd1 = governor.regulate(physics_state, dt=1.0, goal_vector=goal_vec, endocrine_state=None)
    dv2, dd2 = governor.regulate(physics_state, dt=1.0, goal_vector=goal_vec, endocrine_state=MockEndo())
    assert abs(dv2) >= abs(dv1)
    assert abs(dd2) >= abs(dd1)
"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest

def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(20.,10.,0.5,0.5)
    assert solver.nx == pytest.approx(40.), 'Number of nodes in x-axis does not match with given value.'
    assert solver.ny == pytest.approx(20.), 'Number of nodes in y-axis does not match with given value.'

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters()
    """
    solver = SolveDiffusion2D()
    solver.dx = 0.1
    solver.dy = 0.5
    solver.initialize_physical_parameters(10.,125.,300.)
    assert solver.dt == pytest.approx(0.00048, rel=1e-2)

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.T_cold = 130.
    solver.T_hot = 300.
    solver.nx = 1
    solver.ny = 1
    solver.dx = 0.5
    solver.dy = 0.5
    assert solver.set_initial_condition() == pytest.approx(130.)

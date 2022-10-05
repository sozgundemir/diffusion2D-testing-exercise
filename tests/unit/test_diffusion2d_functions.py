"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
from unittest import TestCase

class TestDiffusion2D(TestCase):
    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(20.,10.,0.5,0.5)
        self.assertAlmostEqual(self.solver.nx, 40., 2)
        self.assertAlmostEqual(self.solver.ny, 20., 2)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_physical_parameters()
        """
        self.solver.dx = 0.1
        self.solver.dy = 0.5
        self.solver.initialize_physical_parameters(10.,125.,300.)
        self.assertAlmostEqual(self.solver.dt, 0.00048, 2)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.T_cold = 130.
        self.solver.T_hot = 300.
        self.solver.nx = 1
        self.solver.ny = 1
        self.solver.dx = 0.5
        self.solver.dy = 0.5
        self.assertAlmostEqual(self.solver.set_initial_condition(), 130., 2)
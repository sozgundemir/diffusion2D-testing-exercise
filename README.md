# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/RSE-102/Lecture-Material/blob/main/04_testing/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```
________________________________________ test_initialize_domain _________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(20.,10.,0.5,0.5)
>       assert solver.nx == pytest.approx(40.), 'Number of nodes in x-axis does not match with given value.'
E       AssertionError: Number of nodes in x-axis does not match with given value.
E       assert 20 == 40.0 ± 4.0e-05
E         comparison failed
E         Obtained: 20
E         Expected: 40.0 ± 4.0e-05

tests/unit/test_diffusion2d_functions.py:14: AssertionError
======================================== short test summary info ========================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - AssertionError: Number of no...
```

```
__________________________________ test_initialize_physical_parameters __________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_physical_parameters()
        """
        solver = SolveDiffusion2D()
        solver.dx = 0.1
        solver.dy = 0.5
        solver.initialize_physical_parameters(10.,125.,300.)
>       assert solver.dt == pytest.approx(0.00048, rel=1e-2)
E       assert 0.012019230769230768 == 0.00048 ± 4.8e-06
E         comparison failed
E         Obtained: 0.012019230769230768
E         Expected: 0.00048 ± 4.8e-06

tests/unit/test_diffusion2d_functions.py:25: AssertionError
----------------------------------------- Captured stdout call ------------------------------------------
dt = 0.012019230769230768
======================================== short test summary info ========================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.012019...
```

```
______________________________________ test_set_initial_condition _______________________________________

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
>       assert solver.set_initial_condition() == pytest.approx(130.)
E       assert array([[300.]]) == 130.0 ± 1.3e-04
E         comparison failed
E         Obtained: [[300.]]
E         Expected: 130.0 ± 1.3e-04

tests/unit/test_diffusion2d_functions.py:38: AssertionError
======================================== short test summary info ========================================
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert array([[300.]]) =...
```

Unittest errors

```
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/sinan-demir/git/us_rse102/diffusion2D-testing-exercise/tests/unit/test_diffusion2d_functions.py", line 17, in test_initialize_domain
    self.assertAlmostEqual(self.solver.nx, 40., 2)
AssertionError: 20 != 40.0 within 2 places (20.0 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

```
======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_physical_parameters()
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/sinan-demir/git/us_rse102/diffusion2D-testing-exercise/tests/unit/test_diffusion2d_functions.py", line 27, in test_initialize_physical_parameters
    self.assertAlmostEqual(self.solver.dt, 0.00048, 2)
AssertionError: 0.012019230769230768 != 0.00048 within 2 places (0.011539230769230769 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

```
======================================================================
ERROR: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/sinan-demir/git/us_rse102/diffusion2D-testing-exercise/tests/unit/test_diffusion2d_functions.py", line 39, in test_set_initial_condition
    self.assertAlmostEqual(self.solver.set_initial_condition(), 130., 2)
  File "/usr/lib/python3.8/unittest/case.py", line 957, in assertAlmostEqual
    if round(diff, places) == 0:
TypeError: type numpy.ndarray doesn't define __round__ method

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (errors=1)
```
### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

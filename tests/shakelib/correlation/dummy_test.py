#!/usr/bin/env python

import numpy as np
import pytest

from shakelib.correlation.dummy import DummyCorrelation


def test_dummy_correlation():
    #
    # Pick some common periods
    #
    t1 = np.array([0.01, 0.3, 1.0, 2.0, 3.0])
    dummy = DummyCorrelation(t1)
    #
    # Distances from 0 to 400
    #
    d = np.linspace(0.0, 400.0, 201)
    #
    # Random cross correlations to the periods in t1
    #
    ix1 = np.array(
        [0, 2, 1, 0, 1, 1, 2, 0, 3, 4, 1, 0, 2, 1, 2, 2, 2, 2, 0, 0, 2, 1, 1,
         3, 0, 1, 1, 0, 3, 1, 3, 4, 3, 4, 1, 0, 1, 1, 3, 3, 4, 1, 0, 4, 0, 1,
         1, 3, 3, 2, 0, 1, 1, 0, 2, 3, 2, 0, 1, 4, 2, 4, 4, 4, 3, 2, 1, 1, 3,
         2, 4, 4, 3, 1, 3, 1, 3, 1, 4, 1, 4, 2, 3, 2, 0, 4, 2, 1, 0, 1, 2, 1,
         2, 2, 0, 2, 0, 4, 4, 3, 0, 4, 4, 0, 4, 0, 0, 3, 1, 3, 1, 3, 1, 0, 3,
         3, 1, 1, 4, 0, 1, 2, 4, 1, 3, 4, 1, 0, 3, 4, 1, 4, 2, 4, 4, 4, 2, 4,
         2, 2, 0, 3, 2, 3, 2, 4, 3, 4, 4, 0, 1, 1, 1, 0, 3, 2, 0, 0, 3, 4, 3,
         0, 3, 4, 2, 3, 2, 4, 2, 4, 1, 3, 0, 0, 3, 4, 2, 0, 3, 2, 2, 0, 2, 2,
         0, 2, 4, 2, 0, 0, 0, 1, 1, 2, 3, 2, 0, 3, 0, 1, 4])
    ix2 = np.array(
        [2, 4, 0, 2, 3, 1, 3, 1, 3, 2, 1, 0, 3, 2, 4, 3, 2, 3, 1, 4, 3, 4, 1,
         0, 2, 1, 1, 3, 0, 1, 2, 0, 3, 2, 1, 1, 2, 1, 2, 1, 4, 4, 1, 0, 3, 3,
         0, 4, 4, 0, 1, 1, 0, 2, 3, 0, 1, 4, 1, 3, 4, 3, 4, 2, 3, 4, 3, 4, 0,
         0, 2, 2, 1, 3, 3, 3, 0, 0, 2, 0, 4, 3, 2, 4, 4, 1, 3, 2, 3, 2, 1, 2,
         2, 3, 3, 1, 4, 2, 0, 2, 4, 0, 1, 3, 3, 3, 1, 3, 2, 3, 2, 1, 0, 3, 3,
         0, 1, 2, 0, 1, 3, 3, 2, 4, 0, 2, 0, 1, 2, 4, 4, 2, 3, 4, 2, 2, 4, 2,
         3, 0, 3, 3, 2, 4, 3, 2, 2, 4, 1, 2, 1, 2, 2, 1, 3, 1, 2, 1, 3, 2, 1,
         3, 0, 0, 3, 0, 0, 2, 3, 2, 2, 1, 2, 4, 0, 2, 2, 3, 2, 1, 0, 3, 0, 3,
         1, 0, 2, 1, 4, 2, 4, 2, 3, 4, 4, 3, 2, 0, 1, 4, 1])
    cor = dummy.getCorrelation(ix1, ix2, d)
    cor_target = np.array(
      [1.00000000e-02, 2.72910251e-01, 2.23440015e-02, 5.48811636e-03,
       6.73993446e-02, 3.67879441e-01, 1.50597106e-01, 8.21989880e-03,
       2.01896518e-01, 5.50996294e-02, 1.35335283e-01, 1.10803158e-01,
       4.53589766e-02, 2.22820735e-02, 2.02700209e-02, 2.48935342e-02,
       4.07622040e-02, 1.66866350e-02, 9.10790748e-04, 7.45692395e-05,
       9.15781944e-03, 1.49955768e-03, 1.22773399e-02, 5.02591787e-05,
       8.22974705e-05, 6.73794700e-03, 5.51656442e-03, 2.25829047e-05,
       1.84893186e-05, 3.02755475e-03, 1.23937609e-03, 6.76476879e-06,
       1.66155727e-03, 4.53456013e-04, 1.11377515e-03, 3.03960655e-05,
       2.23975743e-04, 6.11252761e-04, 2.50225717e-04, 6.14602468e-05,
       3.35462628e-04, 2.74653570e-05, 7.49557747e-06, 6.13685979e-07,
       7.53665375e-07, 1.85114706e-05, 3.36798006e-06, 5.51493770e-05,
       4.51524910e-05, 5.54515994e-07, 1.51333099e-06, 3.71703187e-05,
       1.01441610e-06, 2.49160097e-07, 1.01997517e-05, 8.35085040e-08,
       4.10225882e-06, 3.73182828e-08, 9.16608774e-06, 5.00303861e-06,
       2.04807078e-06, 3.35363707e-06, 4.11858871e-06, 1.12400508e-06,
       2.76077257e-06, 7.53443136e-07, 2.77590180e-07, 1.51514411e-07,
       6.20247540e-09, 1.01563147e-08, 2.77176240e-07, 2.26932711e-07,
       8.36085554e-08, 6.84528955e-08, 3.73629938e-07, 4.58853481e-08,
       1.25225819e-09, 6.83508192e-09, 5.59609177e-08, 4.58169243e-09,
       1.12535175e-07, 4.60680042e-08, 3.77172917e-08, 2.05868711e-08,
       1.68551045e-10, 4.13993772e-09, 1.69474716e-08, 8.32524973e-09,
       1.13602300e-10, 5.58058178e-09, 4.56899392e-09, 3.74077584e-09,
       1.02089607e-08, 4.17919505e-09, 3.42163551e-11, 1.68083893e-09,
       1.52906058e-11, 1.25188892e-09, 1.02495996e-11, 1.25874936e-09,
       6.87051207e-12, 5.62509953e-12, 1.38163259e-10, 5.65592546e-12,
       6.17424015e-10, 3.79128021e-12, 2.06935847e-11, 5.08274226e-10,
       1.24841922e-10, 3.40706402e-10, 8.36840428e-11, 3.42573497e-11,
       6.23278793e-12, 7.65446274e-13, 1.25338881e-10, 5.13093982e-13,
       8.40171644e-11, 2.06362309e-11, 1.87727965e-13, 1.53698658e-12,
       5.66270182e-12, 1.54540937e-11, 8.43516121e-12, 2.07183777e-12,
       8.48138647e-14, 4.62931462e-12, 3.79016225e-13, 3.10312239e-13,
       3.81093260e-12, 6.24025543e-12, 5.10908903e-13, 1.39432277e-12,
       1.71236240e-12, 2.80392751e-12, 7.65220560e-13, 6.26509606e-13,
       5.12942681e-13, 4.19961948e-13, 5.15753642e-13, 8.44526736e-15,
       3.45720005e-15, 5.66103201e-13, 4.63486100e-13, 2.52980216e-13,
       1.55342012e-13, 8.47888549e-14, 1.04128865e-13, 1.70507007e-13,
       1.39599331e-14, 1.14294265e-15, 9.35762297e-14, 2.29841211e-14,
       1.88178068e-14, 1.71185746e-15, 4.20465104e-14, 1.03274313e-14,
       2.81846188e-16, 7.69187138e-16, 1.88927149e-14, 5.15601558e-15,
       1.89962483e-15, 5.18427090e-17, 4.24452202e-17, 2.31674714e-17,
       2.84518819e-15, 2.32944307e-17, 3.81437336e-17, 1.04098159e-15,
       1.27842546e-15, 6.97790829e-16, 5.14172529e-16, 2.10484431e-16,
       1.14886718e-17, 3.13537630e-18, 3.85054350e-18, 2.10170559e-16,
       5.16219299e-16, 2.11322308e-18, 1.73016072e-16, 8.49921475e-17,
       2.31952283e-18, 9.49532337e-19, 1.55482265e-18, 6.36490560e-17,
       3.47409597e-18, 8.53304763e-19, 2.32875617e-17, 1.71596186e-17,
       1.56101194e-19, 3.83414545e-19, 1.04637760e-19, 7.71031366e-18,
       3.15633546e-18, 5.74264201e-18, 9.40335524e-18, 5.77411209e-18,
       9.45488627e-20, 3.87050308e-20, 2.11259993e-19, 5.18895161e-19,
       4.24835426e-19])
    np.testing.assert_allclose(cor, cor_target)

    #
    # Test error checks
    #
    ix3 = ix2[1:-1]
    with pytest.raises(ValueError) as e:
        cor = dummy.getCorrelation(ix1, ix3, d)

    d = np.linspace(-1.0, 400.0, 201)
    with pytest.raises(ValueError) as e:
        cor = dummy.getCorrelation(ix1, ix2, d)

    t1 = np.array([0.001, 0.3, 1.0, 2.0, 3.0])
    with pytest.raises(ValueError) as e:
        dummy = DummyCorrelation(t1)

    t1 = np.array([0.01, 0.3, 1.0, 2.0, 3.0, 20.0])
    with pytest.raises(ValueError) as e:  # noqa
        dummy = DummyCorrelation(t1)


if __name__ == '__main__':
    test_dummy_correlation()

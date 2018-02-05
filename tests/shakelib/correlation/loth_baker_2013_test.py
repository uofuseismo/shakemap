#!/usr/bin/env python

import numpy as np
import pytest

import os.path
import sys

from shakelib.correlation.loth_baker_2013 import LothBaker2013

homedir = os.path.dirname(os.path.abspath(__file__))  # where is this script?
shakedir = os.path.abspath(os.path.join(homedir, '..', '..', '..'))
sys.path.insert(0, shakedir)


def test_loth_baker_2012():
    #
    # Pick some common periods
    #
    t1 = np.array([0.01, 0.3, 1.0, 2.0, 3.0])
    lb13 = LothBaker2013(t1)
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
    cor = lb13.getCorrelation(ix1, ix2, d)
    cor_target = np.array(
        [3.70000000e-01, 4.19171915e-01, 3.43437019e-01, 1.96504961e-01,
         1.19085320e-01, 2.29895737e-01, 2.39661117e-01, 1.70447816e-01,
         2.51578254e-01, 1.53015849e-01, 1.27251340e-01, 1.31814088e-01,
         1.27567113e-01, 6.55196545e-02, 9.42114039e-02, 9.64380151e-02,
         9.90563184e-02, 8.05275412e-02, 5.66038175e-02, 1.98105721e-02,
         6.17767116e-02, 1.93930082e-02, 4.16221744e-02, 1.53889002e-02,
         2.18486233e-02, 3.20671662e-02, 2.94099900e-02, 1.08932910e-02,
         9.99471557e-03, 2.27061114e-02, 2.60120877e-02, 7.02001666e-03,
         2.83522448e-02, 1.79356893e-02, 1.47748409e-02, 1.29508794e-02,
         8.68569836e-03, 1.14215495e-02, 1.30918632e-02, 4.82984156e-03,
         1.27227992e-02, 3.47332493e-03, 7.10493216e-03, 2.50806701e-03,
         2.53223662e-03, 2.88763212e-03, 5.04233942e-03, 7.17945168e-03,
         6.58966643e-03, 2.54931413e-03, 3.57865389e-03, 3.43908579e-03,
         3.01485397e-03, 1.80932219e-03, 3.32137978e-03, 9.86294286e-04,
         1.56365986e-03, 7.55374754e-04, 1.88738754e-03, 2.56670473e-03,
         1.77176602e-03, 2.16234541e-03, 1.93004651e-03, 1.37003073e-03,
         1.82405359e-03, 1.15419635e-03, 4.77305945e-04, 3.73986349e-04,
         3.23650592e-04, 4.59100141e-04, 7.51888304e-04, 6.90125496e-04,
         2.85394286e-04, 2.61950978e-04, 7.74078245e-04, 2.20683330e-04,
         1.63032568e-04, 3.53695711e-04, 3.78748857e-04, 2.97974639e-04,
         4.12584495e-04, 3.28272407e-04, 3.01306941e-04, 2.46731793e-04,
         7.46585815e-05, 7.99468361e-05, 2.13849465e-04, 1.09687619e-04,
         5.82869663e-05, 9.24074799e-05, 8.48168003e-05, 7.78496462e-05,
         1.42909598e-04, 1.17363074e-04, 3.48513819e-05, 5.52529763e-05,
         2.66917369e-05, 7.43141870e-05, 2.24867324e-05, 7.01746133e-05,
         1.89441825e-05, 1.73880399e-05, 1.86196784e-05, 1.61136094e-05,
         5.42299270e-05, 1.35750785e-05, 2.94508456e-05, 4.57458663e-05,
         1.81312414e-05, 3.85390828e-05, 1.52748536e-05, 1.00846497e-05,
         1.76094715e-05, 6.83817825e-06, 2.51058638e-05, 5.76089467e-06,
         1.30856585e-05, 8.38301741e-06, 4.04968763e-06, 9.66428286e-06,
         4.66265890e-06, 1.06469379e-05, 8.71847845e-06, 3.07781214e-06,
         2.66356171e-06, 6.74163094e-06, 5.30387089e-06, 4.86819204e-06,
         5.84316338e-06, 6.18694232e-06, 1.68913912e-06, 4.03100676e-06,
         4.14712442e-06, 4.39111794e-06, 3.11700718e-06, 2.86096511e-06,
         2.62595524e-06, 2.41024993e-06, 2.47967987e-06, 1.13799507e-06,
         6.75863359e-07, 2.48138214e-06, 1.96697722e-06, 1.91626077e-06,
         1.48266887e-06, 1.21411590e-06, 1.24908987e-06, 1.32257931e-06,
         3.61086354e-07, 4.82934205e-07, 7.09802262e-07, 4.54718018e-07,
         4.17365861e-07, 5.24217395e-07, 8.14264527e-07, 3.22731383e-07,
         2.65039911e-07, 3.72057842e-07, 5.77915776e-07, 3.65684683e-07,
         1.51225139e-07, 1.11719462e-07, 1.02542427e-07, 8.55629338e-08,
         2.67017265e-07, 7.92917257e-08, 1.12475741e-07, 1.84206453e-07,
         1.89512726e-07, 1.55186650e-07, 8.92200740e-08, 5.89042104e-08,
         6.72523426e-08, 3.63105857e-08, 3.66606953e-08, 9.27903706e-08,
         1.06694277e-07, 2.83481664e-08, 8.04240546e-08, 4.12510880e-08,
         3.38770423e-08, 2.01198162e-08, 2.85400680e-08, 5.23913704e-08,
         3.67729903e-08, 2.20688285e-08, 3.61430880e-08, 2.07794227e-08,
         1.00381720e-08, 1.56631214e-08, 8.45676285e-09, 1.47479790e-08,
         9.73680049e-09, 1.98357472e-08, 2.42084678e-08, 1.87308231e-08,
         8.59610329e-09, 5.10528684e-09, 1.10758118e-08, 4.56166901e-09,
         4.18695727e-09])
    np.testing.assert_allclose(cor, cor_target)

    #
    # Test error checks
    #
    ix3 = ix2[1:-1]
    with pytest.raises(ValueError) as e:
        cor = lb13.getCorrelation(ix1, ix3, d)

    d = np.linspace(-1.0, 400.0, 201)
    with pytest.raises(ValueError) as e:
        cor = lb13.getCorrelation(ix1, ix2, d)

    t1 = np.array([0.001, 0.3, 1.0, 2.0, 3.0])
    with pytest.raises(ValueError) as e:
        lb13 = LothBaker2013(t1)

    t1 = np.array([0.01, 0.3, 1.0, 2.0, 3.0, 20.0])
    with pytest.raises(ValueError) as e:  # noqa
        lb13 = LothBaker2013(t1)


if __name__ == '__main__':
    test_loth_baker_2012()

import pytest
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.cm as cm
import datetime

import sys
import pprint
sys.path.append(sys.path[0].replace('/tests',''))
sys.path.append("./src/outputCSVfromAppMapMatching")
pprint.pprint(sys.path)


from src.plot_dens import v, pn, conj, plot_original_dens


def test_v():
    """This is a
    """
    x=np.random.uniform(-5, 5)
    y=np.random.uniform(-5, 5)
    B_num =  [0, 1, 3, 4, 6, 7, 8, 9, 10, 12, 15, 16, 19, 20, 21, 24, 25, 26, 30, 31, 36, 37]
    return v(x, y, B_num)



#K(x1,x2) = v(x2)^T v(x1)
def test_pn_1():
    x = np.random.uniform(-5, 5)
    y = np.random.uniform(-5, 5)
    B_num =  [0, 1, 3, 4, 6, 7, 8, 9, 10, 12, 15, 16, 19, 20, 21, 24, 25, 26, 30, 31, 36, 37]
    return pn(x,y,B_num)

def test_pn_2():
    x = 2.902196162544687
    y = -4.279161176188579
    B_num =  [0, 1, 3, 4, 6, 7, 8, 9, 10, 12, 15, 16, 19, 20, 21, 24, 25, 26, 30, 31, 36, 37]
    return pn(x,y,B_num)

def test_conj():
    e_1 =  [7.84587719e-04+0.j, 3.90091675e-03+0.00728538j, 1.40642767e-03+0.0009134j, -5.61505107e-05+0.00066383j]
    return conj(e_1)





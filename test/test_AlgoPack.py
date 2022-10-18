import numpy as np
import numpy.testing as npt

import AlgoPack

def test_AugoPack_smoke():
    #Smoke_test
    obt = AlgoPack.AlgoPack_object()

def test_AutoPack_object_fizz():
    #test the fizz_function
    obj = AlgoPack.AlgoPack_object()
    output = obj.fizz()

    npt.assert_equal(output, "buzz")

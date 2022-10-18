import numpy as np
import numpy.testing as npt
from AlgoPack import Node

def test_node():
    #test the fizz_function
    obj = Node("buzz")

    assert(obj.value, "buzz")
    assert(obj.next, None)

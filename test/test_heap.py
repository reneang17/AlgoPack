from AlgoPack import Heap
import pytest


def test_heap():
    heap_size = 5
    heap = Heap(heap_size)

    assert heap.size() == 0
    assert heap.get_minimum() == None

    elements = [1, 2, 3, 4, 1, 2]
    for element in elements:
        heap.insert(element)

    assert heap.size() == 6
    assert heap.cbt == [1, 1, 2, 4, 2, 3, None, None, None, None]
    assert heap.get_minimum() == 1

    for _ in range(2):
        heap.remove()
    assert heap.size() == 4
    assert heap.cbt == [2, 3, 2, 4, 1, 1, None, None, None, None]

    for _ in range(4):
        heap.remove()

    assert heap.size() == 0
    assert heap.get_minimum() == None
    assert heap.cbt == [4, 3 , 2, 2, 1, 1, None, None, None, None]

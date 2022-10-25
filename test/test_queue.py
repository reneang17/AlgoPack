from AlgoPack import Queue
import pytest

def test_queue():
    # Setup
    q = Queue()

    assert q.size() == 0
    assert q.dequeue() == None

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 3

    assert q.dequeue() == 1

    q.enqueue(4)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.dequeue() == None
    q.enqueue(5)
    assert q.size() == 1

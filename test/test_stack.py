from AlgoPack import Stack
import pytest

def test_Stack():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)

    # Test size
    assert stack.size() == 5

    # Test pop
    assert stack.pop() == 50

    # Test push
    stack.push(60)
    assert stack.pop() == 60
    assert stack.pop() == 40
    assert stack.pop() == 30
    stack.push(50)
    
    assert stack.size() == 3

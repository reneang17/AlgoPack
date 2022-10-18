from AlgoPack import LinkedList
import pytest

def test_Linkedlist():
    # Test prepend
    linked_list = LinkedList()
    assert linked_list.head== None

def test_prepend():
    # Test prepend
    linked_list = LinkedList()
    # appends retuns None
    assert linked_list.prepend(1) == None

    assert linked_list.head.value == 1
    linked_list.prepend(2)
    linked_list.prepend(3)
    assert linked_list.head.value == 3
    assert linked_list.head.next.next.value == 1

def test_append():
    # Test append
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)

    assert linked_list.append(3) == None
    node = linked_list.head
    assert node.value == 1
    assert node.next.next.value == 3


def test_search():
    # Test search
    # Empty list
    linked_list = LinkedList()
    assert linked_list.search('tacocat') == None
    for i in range(0,10):
        linked_list.append(i)
    node = linked_list.search(5)
    assert node.value == 5
    with pytest.raises(ValueError):
        linked_list.search(-1)


def test_remove():
    # Test search
    # Empty list
    linked_list = LinkedList()

    #edge case: empty list
    assert linked_list.remove('tacocat') == None

    for i in range(0,10):
        linked_list.append(i)

    #edge case: no found element
    with pytest.raises(ValueError):
        linked_list.remove('tacocat')

    #edge case: remove first element
    assert linked_list.remove(0) == None
    assert linked_list.head.value == 1

    #edge case: remove last element
    linked_list.remove(9)
    node = linked_list.head
    while node.next:
        node=node.next
    assert node.value == 8

    linked_list.remove(5)
    node = linked_list.head
    i=1
    while i<=4:
        node = node.next
        i+=1
    assert node.value == 6


def test_pop():
    # Test pop
    linked_list = LinkedList()
    assert linked_list.pop() == None
    for i in range(1,10):
        linked_list.append(i)
    for i in range(1,10):
        assert linked_list.pop() == i
    assert linked_list.pop() == None

def test_insert():
    # Test pop
    linked_list = LinkedList()

    linked_list.insert('cat',0)
    assert linked_list.head.value == 'cat'
    linked_list.pop()

    linked_list.insert('cat',100)
    assert linked_list.head.value == 'cat'
    linked_list.pop()

    for i in range(0,10):
        linked_list.append(i)

    linked_list.insert('dog',100)
    node =  linked_list.head
    while node.next:
        node = node.next
    assert node.value == 'dog'

    linked_list.insert('rat',5)
    node =  linked_list.head
    for i in range(0,5):
        node= node.next
    assert node.value == 'rat'


def test_size():
    # Test size
    linked_list = LinkedList()
    assert linked_list.size() == 0
    for i in range(1,10):
        linked_list.append(i)
    assert linked_list.size() == 9

def test_to_list():
    linked_list = LinkedList()
    assert linked_list.to_list() == []
    for i in range(0,5):
        linked_list.append(i)
    assert linked_list.to_list() == [0,1,2,3,4]    

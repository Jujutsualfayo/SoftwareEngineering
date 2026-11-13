import pytest
from min_heap import MinHeap


def test_insert_into_empty_heap():
    heap = MinHeap()
    heap.insert(10)

    assert heap.heap == [10]


def test_insert_smaller_value():
    heap = MinHeap()
    heap.insert(10)
    heap.insert(5)

    assert heap.heap == [5, 10]


def test_insert_multiple_values():
    heap = MinHeap()

    for value in [10, 5, 8, 2, 12, 3]:
        heap.insert(value)

    assert heap.peek() == 2


def test_insert_duplicate_values():
    heap = MinHeap()

    for value in [5, 5, 3, 3]:
        heap.insert(value)

    assert heap.peek() == 3

def test_extract_min_from_single_element():
    heap = MinHeap()
    heap.insert(10)

    assert heap.extract_min() == 10
    assert heap.heap == []


def test_extract_min_from_multiple_elements():
    heap = MinHeap()
    for value in [2, 5, 3, 10, 12, 8]:
        heap.insert(value)

    assert heap.extract_min() == 2
    assert heap.peek() == 3


def test_extract_min_from_empty_heap():
    heap = MinHeap()

    with pytest.raises(IndexError):
        heap.extract_min()

def test_extract_min_returns_sorted_order():
    heap = MinHeap()
    for value in [2, 5, 3, 10, 12, 8]:
        heap.insert(value)

    result = []
    while heap.heap:                      # loop until the heap is empty
        result.append(heap.extract_min())

    assert result == [2, 3, 5, 8, 10, 12]
def test_heapify_root_and_input_unchanged():
    numbers = [10, 5, 3, 8, 2, 7, 4, 9]
    heap = MinHeap()
    heap.heapify(numbers)

    # 1. the root is the minimum
    assert heap.peek() == 2

    # 2. the original list was not modified
    assert numbers == [10, 5, 3, 8, 2, 7, 4, 9]
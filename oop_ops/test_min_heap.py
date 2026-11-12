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
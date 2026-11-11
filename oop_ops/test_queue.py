from my_queue import Queue


def test_new_queue_is_empty():
    queue = Queue()

    assert queue.is_empty() is True
    assert queue.size() == 0


def test_enqueue_increases_size():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)

    assert queue.size() == 2
    assert queue.is_empty() is False


def test_dequeue_follows_fifo():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    assert queue.dequeue() == 10
    assert queue.dequeue() == 20


def test_peek_does_not_remove_element():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)

    assert queue.peek() == 10
    assert queue.size() == 2


def test_dequeue_from_empty_queue():
    queue = Queue()

    assert queue.dequeue() is None
    assert queue.is_empty() is True


def test_queue_becomes_empty_after_all_elements_removed():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)

    queue.dequeue()
    queue.dequeue()

    assert queue.is_empty() is True
    assert queue.size() == 0
    
def test_pop_behaviour():
    queue = Queue()
    
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
    queue.dequeue()
    
    assert queue.peek() == 20
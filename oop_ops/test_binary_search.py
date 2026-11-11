from binary_search import binary_search


def test_find_existing_number():
    numbers = [10, 20, 30, 40, 50]

    assert binary_search(numbers, 30) == 2


def test_find_first_number():
    numbers = [10, 20, 30, 40, 50]

    assert binary_search(numbers, 10) == 0


def test_find_last_number():
    numbers = [10, 20, 30, 40, 50]

    assert binary_search(numbers, 50) == 4


def test_number_not_found():
    numbers = [10, 20, 30, 40, 50]

    assert binary_search(numbers, 100) == -1


def test_empty_list():
    assert binary_search([], 10) == -1
    



# Linear search is sequential algorithm that compare each item in the list
# until the target item is found.


def linear_search(vals, target):
    """
    :param vals: A list of values
    :param target: A value you want to search
    :return: The target value if found or None if not found
    """
    num_ops = 0
    for each_val in vals:
        num_ops += 1
        if each_val == target:
            return (num_ops, each_val)
    return (num_ops, None)


def test_linear_search():
    vals = [1, 5, 6, 9, 3, 2 ,7, 3, 1, 11]

    # Test value in the list
    target = 7
    expect = (7, 7)
    found = linear_search(vals, target)
    assert found == expect

    # Test value not in the list
    target = 0
    expect = (10, None)
    found = linear_search(vals, target)
    assert found == expect


if __name__ == '__main__':
    test_linear_search()
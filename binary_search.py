# Binary search implementation using while loop
# 1. Started with a sorted list
# 2. Find the mid-point of the list
# 3. Compare the value in the mid-point position to the target
# 4. If match, target found and end
# 5. If not, decide whether the target value is in the lower half or
#    upper half of the sub-list
# 6. Repeat step 2 to 4 until either the target is found and at the end
#    of the list


def binary_search(vals, target):
    """
    Search a target value using the binary search algorithm.

    :param vals: A list of values
    :param target: The target value
    :return: The target value if found or None if not found
    """

    pos_begin = 0
    pos_end = len(vals) - 1

    while pos_begin <= pos_end:
        pos_mid = (pos_begin + pos_end) // 2

        if target == vals[pos_mid]:
            return target
        elif target > vals[pos_mid]:
            pos_begin = pos_mid + 1
        else:
            pos_end = pos_mid - 1
    return None


def test_binary_search():

    # Test value in a single item list
    vals = [7]
    target = 7
    expect = 7
    found = binary_search(vals, target)
    assert found == expect

    # Test value not in a single item list
    vals = [7]
    target = 0
    expect = None
    found = binary_search(vals, target)
    assert found == expect

    # Test value in the first position of a two items list
    vals = [1, 3]
    target = 3
    expect = 3
    found = binary_search(vals, target)
    assert found == expect

    # Test value in the last position of a two items list
    vals = [1, 3]
    target = 1
    expect = 1
    found = binary_search(vals, target)
    assert found == expect

    # Test with sorted values and target at the mid-point
    vals = [1, 3, 5, 7, 10]
    target = 5
    expect = 5
    found = binary_search(vals, target)
    assert found == expect

    # Test with sorted values and target at the lower half of the sub-list
    vals = [1, 3, 5, 7, 10, 12]
    target = 3
    expect = 3
    found = binary_search(vals, target)
    assert found == expect

    # Test with sorted values and target at the upper half of the sub-list
    vals = [1, 3, 5, 7, 10, 12]
    target = 12
    expect = 12
    found = binary_search(vals, target)
    assert found == expect

    # Test with sorted values and target is not in the list
    vals = [1, 3, 5, 7, 10, 12]
    target = 13
    expect = None
    found = binary_search(vals, target)
    assert found == expect


if __name__ == '__main__':
    test_binary_search()
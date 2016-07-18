"""
Review of binary search
More information see https://en.wikipedia.org/wiki/Binary_search_algorithm

Average runtime: O(log(n))
Worst-case space complexity: O(log(n)) - recursive, O(1) - iterative

Tests are included as simple series of assert functions rather than using a
test runner (unittest, pytest, etc...)
"""
from math import ceil

def binary_search_recursive(sorted_list_to_search, value_to_find):
    """
    Binary Search Recursive
    """
    # two base cases
    if len(sorted_list_to_search) is 0:
        return False
    elif len(sorted_list_to_search) is 1:
        return sorted_list_to_search[0] == value_to_find

    # grab the middle index for simplicity
    middle_index = ceil(len(sorted_list_to_search)/2)

    # return prematurely if the value to find is equal to the middle index
    if sorted_list_to_search[middle_index] == value_to_find:
        return True
    # otherwise check which side should be checked next
    elif sorted_list_to_search[middle_index] > value_to_find:
        return binary_search_recursive(sorted_list_to_search[0:middle_index], value_to_find)
    else:
        return binary_search_recursive(sorted_list_to_search[middle_index:], value_to_find)

def binary_search_iterative(sorted_list_to_search, value_to_find):
    """
    Binary Search iterative
    """
    while len(sorted_list_to_search) > 1:
        middle = ceil(len(sorted_list_to_search)/2)
        if sorted_list_to_search[middle] == value_to_find:
            return True
        elif sorted_list_to_search[middle] > value_to_find:
            sorted_list_to_search = sorted_list_to_search[0:middle]
            continue

        sorted_list_to_search = sorted_list_to_search[middle:]

    return sorted_list_to_search[0] == value_to_find




def test_binary_search_recursive():
    """
    run binary search test cases
    """
    def case1(search_method):
        """Simple true numeric case"""
        simple_list = [1, 2, 3, 4, 5]
        value_to_find = 1
        result = search_method(simple_list, value_to_find)
        assert(result)

    def case2(search_method):
        """Simple true alpha case"""
        alpha_list = ['a', 'b', 'c', 'd', 'e']
        value_to_find = 'a'
        result = search_method(alpha_list, value_to_find)
        assert(result)

    def case3(search_method):
        """Simple false numeric case"""
        simple_list = [1, 2, 3, 4, 5]
        value_to_find = 6
        result = search_method(simple_list, value_to_find)
        assert(result is False)

    def case4(search_method):
        """Simple false alpha case"""
        alpha_list = ['a', 'b', 'c', 'd', 'e']
        value_to_find = 'f'
        result = search_method(alpha_list, value_to_find)
        assert(result is False)

    cases = [case1, case2, case3, case4]
    for case in cases:
        for search in [binary_search_recursive, binary_search_iterative]:
            case(search)


def main():
    test_binary_search_recursive()

if __name__ == "__main__":
    main()

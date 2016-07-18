"""
Review of merge sort
More information see https://en.wikipedia.org/wiki/Merge_sort
"""
from math import ceil

def merge_sort(list_to_sort):
    pass


def test_merge_sort():
    simple_test_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    resulting_list = merge_sort(simple_test_list)
    expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert(resulting_list == expected_list)

def main():
    test_merge_sort()

if __name__ == "__main__":
    main()

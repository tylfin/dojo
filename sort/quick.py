"""
Review of quick sort
More information see https://en.wikipedia.org/wiki/Quicksort

Average runtime: O(n*log(n)) (can be written O(n) best case with three-way
    partition)
Worst runtime: O(n^2)
Worst-case space complexity: O(nlog(n))
"""
from math import ceil

def quick_sort(list_to_sort):
    if len(list_to_sort) < 2:
        return list_to_sort

    middle = ceil(len(list_to_sort)/2)
    middle_val = list_to_sort[middle]

    left, right = [], []

    for val in list_to_sort[0:middle] + list_to_sort[middle+1:]:
        if val < middle_val:
            left.append(val)
        else:
            right.append(val)
    return quick_sort(left) + [middle_val] + quick_sort(right)


def test_quick_sort():
    simple_test_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    resulting_list = quick_sort(simple_test_list)
    expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert(resulting_list == expected_list)

def main():
    test_quick_sort()

if __name__ == "__main__":
    main()

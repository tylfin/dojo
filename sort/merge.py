"""
Review of merge sort
More information see https://en.wikipedia.org/wiki/Merge_sort
"""
from math import ceil

def merge_sort(list_to_sort):
    # base case
    if len(list_to_sort) < 2:
        return list_to_sort
    # grab the middle for simplicity
    middle = ceil(len(list_to_sort)/2)

    # split into two lists
    left = merge_sort(list_to_sort[:middle])
    right = merge_sort(list_to_sort[middle:])

    merged_list = []
    while len(left) or len(right):
        # if the right, or left is empty dump the other list onto the end
        if not len(right):
            merged_list += left
            left = []
        elif not len(left):
            merged_list += right
            right = []
        # otherwise pop the lesser of the two onto the merged list
        elif left[0] < right[0]:
            merged_list.append(left.pop(0))
        else:
            merged_list.append(right.pop(0))

    return merged_list


def test_merge_sort():
    simple_test_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    resulting_list = merge_sort(simple_test_list)
    expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(resulting_list)
    assert(resulting_list == expected_list)

def main():
    test_merge_sort()

if __name__ == "__main__":
    main()

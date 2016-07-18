"""
Review of insertion sort
More information see https://en.wikipedia.org/wiki/Insertion_sort
"""
from math import ceil

def insertion_sort(sorting_list):
    for current_index in range(len(sorting_list)):
        value_to_insert = sorting_list[current_index]
        index_to_check = current_index - 1

        while (index_to_check >= 0) and (sorting_list[index_to_check] > value_to_insert):
            sorting_list[index_to_check + 1] = sorting_list[index_to_check]
            index_to_check -= 1

        sorting_list[index_to_check+1] = value_to_insert

    return sorting_list

def test_insertion_sort():
    simple_test_list = [9, 8, 7, 6, 5, 4, 3, 1, 1, 1, 2, 1]
    resulting_list = insertion_sort(simple_test_list)
    expected_list = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert(resulting_list == expected_list)

def main():
    test_insertion_sort()

if __name__ == "__main__":
    main()

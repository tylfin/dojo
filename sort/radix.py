"""
Review of radix sort
https://en.wikipedia.org/wiki/Radix_sort

Example sort:
list_to_sort = [10, 11, 12, 13, 101]

Iteration 1:
buckets = [[10], [11, 101], [12], [13]]
list_to_sort = [10, 11, 101, 12, 13]

Iteration 2:
buckets = [[10, 11, 12, 13], [101]]
list_to_sort = [10, 11, 12, 13, 101]
"""

def radix_sort(list_to_sort):
    RADIX = 10 # base ten
    place = 1
    done = False

    while not done:
        done = True
        buckets = [list() for _ in range(RADIX)]

        for value in list_to_sort:
            tmp = value / place
            buckets[tmp].append(value)
            if tmp > 0 and done:
                done = False

        index = 0
        for bucket in buckets:
            for value in bucket:
                list_to_sort[index] = value
                index += 1

        place += 1

    return list_to_sort


def test_radix_sort():
    simple_test_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    resulting_list = radix_sort(simple_test_list)
    print(resulting_list)
    expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert(resulting_list == expected_list)

def main():
    test_radix_sort()

if __name__ == "__main__":
    main()

# given an array of integers that are out of orders determine the bounds of the smallest window
# that must be sorted in order for the entire array to be sorted
# for example given [3,7,5,6,9] should return  [1,3]

# Solution using sorting takes O(n log n) time and O(n) space
def smallest_window_to_sort(array):
    sorted_array = sorted(array)
    start_index = 0
    end_index = 0
    for i in range(len(array)):
        if not sorted_array[i] == array[i]:
            start_index = i
            break
    for i in reversed(range(len(array))):
        if not sorted_array[i] == array[i]:
            end_index = i
            break
    return start_index, end_index


# Solution  takes O(n) time and O(1) space
def smallest_window_to_sort1(array):
    max_seen, min_seen = -float("inf"), float("inf")
    start_index, end_index = None, None
    for i in range(len(array)):
        max_seen = max(array[i], max_seen)
        if array[i] < max_seen:
            end_index = i

    for i in reversed(range(len(array))):
        min_seen = min(array[i], min_seen)
        if array[i] > min_seen:
            start_index = i
    return start_index, end_index


if __name__ == '__main__':
    print(smallest_window_to_sort([3, 7, 5, 6, 9]))
    print(smallest_window_to_sort1([3, 7, 5, 6, 9]))

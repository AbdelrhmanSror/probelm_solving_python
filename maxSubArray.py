# given an array , find the maximum subarray sum of any contiguous subarray of the array.
# e.g. array [34,-50,42,14,-5,86]  max sum would be 137 since we would take elements 42,14,-5 and 86
# e.g. array [-5,-1,-8,-9] the max would be 0 ,since we would not take any element.

# do this in O(n) time

# takes O(n) time and O(1) space
# kadane's algorithm
def max_sub_array(array):
    max_so_far, max_ending_here = 0, 0
    for item in array:
        max_ending_here = max(item, max_ending_here + item)
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far


# follow-up : what if element can wrap around ?
# e.g. array [8,-1,3,4] return 15 cause we would take 3,4,8 obtained from wrapping around.
def min_sub_array(array):
    min_so_far, min_ending_here = 0, 0
    for item in array:
        min_ending_here = min(item, min_ending_here + item)
        min_so_far = min(min_ending_here, min_so_far)
    return min_so_far


def max_circular_subarray(array):
    max_wrap_around = sum(array) + min_sub_array(array)
    return max(max_wrap_around, max_sub_array(array))


if __name__ == '__main__':
    print(max_sub_array([8, -1, 3, 4]))
    print(max_circular_subarray([8, -1, 3, 4]))

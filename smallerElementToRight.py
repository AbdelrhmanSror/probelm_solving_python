# given an array of integers ,return a new array where each element in the new array is the number
# of smaller elements to the right of that element in the original input array:
# e.g. [3,4,9,6,1] return [1,1,2,1,0]

# this solution take O(n) time and O(n) space
import bisect


def smaller_counts(array):
    result = []
    for i, number in enumerate(array):
        count = sum(item < number for item in array[i + 1:])
        result.append(count)
    return result


# best case scenario would take O(n) time and O(n) space
# worest case scenario when they are already sorted would take O(n^2) time and O(n) space
def smaller_counts2(array):
    result = [0] * len(array)
    for i in range(len(array) - 1, -1, -1):
        index_counter = i + 1
        while index_counter < len(array):
            if array[index_counter] < array[i]:
                count = 1 + result[index_counter]
                result[i] = count
                break
            index_counter += 1
    return result

# run in nlog(n) time and o(n) space
def smaller_counts3(array):
    result = []
    seen = []
    for number in reversed(array):
        # finding the best location to insert in it the number in a way that does not disturb the sorted manner
        proper_location = bisect.bisect_left(seen, number)
        result.append(proper_location)
        bisect.insort(seen, number)
    return list(reversed(result))


if __name__ == '__main__':
    print(smaller_counts3([3, 4, 9, 6, 1]))

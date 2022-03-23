# given arrays of integers,return a new array such that each element at index i of the new array is the product of
# all element in the original array. e.g. input : [1 , 2 , 3 ,4 , 5]    output:[120 ,60 ,40 , 30 ,24]
# e.g. input : [3 , 2 , 1 ]   output :[2 ,3 , 6]
def product_with_division(array):
    multiplication = 1
    for number in array:
        multiplication *= number

    output = [multiplication / number for number in array]

    return output


def product_without_division(array):
    # list represent the product of all element before number at current index
    product_before = []
    # list represent the product of all element after number at current index
    product_after = []
    for i in range(len(array)):
        if i == 0:
            product_before.append(1)
            continue
        product_before.append(array[i - 1] * product_before[i - 1])

    for i in reversed(range(len(array))):
        if i == len(array) - 1:
            product_after.append(1)
            continue
        product_after.insert(0, array[i + 1] * product_after[0])
    multiplication=[product_before[i]*product_after[i] for i in range(len(array))]
    return multiplication


if __name__ == '__main__':
    print(product_without_division([1,2,3,4,5]))

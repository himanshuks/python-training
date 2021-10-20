# Linear search has O(n)
# Simple iterate through each element one by one in list

from decorators import cal_time


@cal_time
def linear_search(list, find):
    for index, element in enumerate(list):
        if element == find:
            return index
    return -1


# Binary search has O(log n)
# Divide sorted list into 2 parts using middle value
# Then search only in their respective half section


@cal_time
def binary_search(list, find):

    left_index = 0
    right_index = len(list) - 1
    mid_index = 0

    while left_index <= right_index:

        # Using // returns integer part of decimal value
        # Like 2.5 gives -> 2
        # Else use / for simple multiplication
        mid_index = (left_index + right_index) // 2

        if find == list[mid_index]:
            return mid_index

        elif find < list[mid_index]:
            right_index = mid_index - 1

        else:
            left_index = mid_index + 1

    return -1


def recursive_binary_search(list, find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2

    if find == list[mid_index]:
        return mid_index

    elif find < list[mid_index]:
        right_index = mid_index - 1

    else:
        left_index = mid_index + 1

    return recursive_binary_search(list, find, left_index, right_index)


number_list = [12, 15, 17, 19, 21, 24, 45, 67]
find_num = 21

big_number_list = [i for i in range(1, 10000001)]
new_find_num = 10000000

exercise_list = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
exercise_num = 15

ls = linear_search(big_number_list, new_find_num)
bs = binary_search(big_number_list, new_find_num)

rbs = recursive_binary_search(big_number_list, new_find_num, 0, len(big_number_list))

exer = binary_search(exercise_list, exercise_num)

print(f"Element found at {ls} index using linear search")
print(f"Element found at {bs} index using binary search")
print(f"Element found at {rbs} index using recursive binary search")
print(f"Element found at {exer} index using recursive binary search")

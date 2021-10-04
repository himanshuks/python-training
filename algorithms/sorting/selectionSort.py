# Selection sort will place smallest element the left side in each iteration
def selection_sort(list):
    size = len(list)

    # Go till SIZE -1 as last element will already be sorted due to other elements being in place
    for i in range(size - 1):
        min_index = i

        # Second loop will move current pointer to next element
        for j in range(min_index + 1, size):
            if list[j] < list[min_index]:
                min_index = j

        # Used to swap the elements
        if i != min_index:
            list[i], list[min_index] = list[min_index], list[i]


number_list = [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1]

selection_sort(number_list)
print(number_list)

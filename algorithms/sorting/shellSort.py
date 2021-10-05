# Shell sort function
# We jump in array with fixed gap
def shell_sort(list):

    # Make gap half the size of incoming array
    size = len(list)
    gap = size // 2

    # Till gap becomes 1, compare the ANCHOR element with iterable element
    while gap > 0:
        for i in range(gap, size):

            anchor = list[i]
            j = i

            # Swap elements if iterable element is greater than ANCHOR element
            # While is used till we get element at position of Anchor - GAP
            while j >= gap and list[j - gap] > anchor:

                # Step 1 of swap
                list[j] = list[j - gap]
                j -= gap

            # Step 2 of swap
            list[j] = anchor

        # After first run, heavier elements come to right side
        # Reduce the gap and repeat the process
        gap = gap // 2


number_list = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]

shell_sort(number_list)
print(number_list)
print(set(number_list))
print(list(set(number_list)))


tests = [
    [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
    [],
    [1, 5, 8, 9],
    [234, 3, 1, 56, 34, 12, 9, 12, 1300],
    [5],
]

for x in tests:
    shell_sort(x)
    print("Sorted array using Shell Sort :", x)

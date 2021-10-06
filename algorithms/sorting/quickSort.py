# Swap function take 2 index and array
def swap_items(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


# Function to create partition with pointers
def create_partition_hoare(list, start_pointer, end_pointer):
    pivot_index = start_pointer
    pivot = list[pivot_index]

    # This loop works till element gets its right position
    while start_pointer < end_pointer:

        # Move START to right till it gets number greater than PIVOT
        while start_pointer < len(list) and list[start_pointer] <= pivot:
            start_pointer += 1

        # Move END to left till it gets number less than PIVOT
        while list[end_pointer] > pivot:
            end_pointer -= 1

        # Swap START and END
        if start_pointer < end_pointer:
            swap_items(start_pointer, end_pointer, list)

    # Once swapping is complete, swap END with PIVOT
    # This way first element gets it correct position
    swap_items(pivot_index, end_pointer, list)
    return end_pointer


# Function to create partition with pointers
def create_partition_lomuto(list, start_pointer, end_pointer):
    p_index = start_pointer
    pivot = list[end_pointer]

    # Move P index from START to END, swap ITR with PIVOT
    for i in range(start_pointer, end_pointer):
        if list[i] <= pivot:
            swap_items(i, p_index, list)
            p_index += 1

    # Once swapping is complete, swap END with P index
    # This way last element gets it correct position
    swap_items(p_index, end_pointer, list)
    return p_index


# Sort the array using HAORE partition
def quick_sort_hoare(elements, start, end):
    if start < end:

        # Get the pointer just LEFT of PIVOT after correct placement
        pi = create_partition_hoare(elements, start, end)

        # Repeat sort for LEFT & RIGHT partition
        quick_sort_hoare(elements, start, pi - 1)
        quick_sort_hoare(elements, pi + 1, end)


# Sort the array using LOMUTO partition
def quick_sort_lomuto(elements, start, end):
    if start < end:

        # Get the pointer just LEFT of PIVOT after correct placement
        pi = create_partition_lomuto(elements, start, end)

        # Repeat sort for LEFT & RIGHT partition
        quick_sort_lomuto(elements, start, pi - 1)
        quick_sort_lomuto(elements, pi + 1, end)


number_list = [11, 9, 29, 7, 2, 15, 28]
print(number_list)

quick_sort_hoare(number_list, 0, len(number_list) - 1)

print(number_list)

tests = [
    [11, 9, 29, 7, 2, 15, 28],
    [3, 7, 9, 11],
    [25, 22, 21, 10],
    [29, 15, 28],
    [],
    [6],
]

for x in tests:
    quick_sort_hoare(x, 0, len(x) - 1)
    print("Sorted array HOARE:", x)


for x in tests:
    quick_sort_lomuto(x, 0, len(x) - 1)
    print("Sorted array LOMUTO:", x)

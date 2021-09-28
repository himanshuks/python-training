# Bubble sort swaps 2 consecutive elements and place highest element at the end in each iteration


def bubble_sort(list):
    size = len(list)

    # Run two loops
    # First to iterate each element
    # Second to swap consecutive elements
    for i in range(size - 1):

        # Flag is placed to pause loop if next coming elements are already sorted
        swapped = False
        for j in range(size - 1 - i):
            if list[j] > list[j + 1]:
                tmp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = tmp
                swapped = True
        if not swapped:
            break

    return list


def bubble_sort_dictionary_input(list, key):
    size = len(list)

    # Size-1 is done as last element left will already be the loweset and at leftest position
    for i in range(size - 1):

        swapped = False
        for j in range(size - 1 - i):

            # a,b will store the key value from dictionary
            a = list[j][key]
            b = list[j + 1][key]

            if a > b:
                tmp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = tmp
                swapped = True

        # Break the current loop if swap is done
        if not swapped:
            break

    return list


number_list = [5, 2, 9, 1, 67, 34, 88, 34]

elements = [
    {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
    {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
    {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
    {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
]

print("Sorted list :", bubble_sort(number_list))
print("Sorted list :", bubble_sort_dictionary_input(elements, key="device"))

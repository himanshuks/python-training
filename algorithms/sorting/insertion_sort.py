def insertion_sort(list):
    for i in range(1, len(list)):
        anchor = list[i]
        j = i - 1
        while j >= 0 and anchor < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = anchor


number_list = [11, 9, 29, 7, 2, 15, 28]

insertion_sort(number_list)

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
    insertion_sort(x)
    print("Sorted array by Insertion :", x)

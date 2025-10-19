import random

def binary_search(array, target):
    if len(array) == 0:
        print("Element not found")
        return

    first_index = 0
    last_index = len(array) - 1
    mid_index = (first_index + last_index) // 2

    if target > array[mid_index]:
        new_array = array[mid_index + 1:]   # right side
        binary_search(new_array, target)

    elif target < array[mid_index]:
        new_array = array[:mid_index]       # left side (fixed here)
        binary_search(new_array, target)

    else:  # target == array[mid_index]
        print("Element found at index", mid_index)
        return


def MAIN():
    length = int(input("Enter the length of the array: "))
    array = []

    for _ in range(length):
        array.append(random.randint(1, 100))

    print("-" * 40)
    target = int(input("Enter the element to be searched: "))
    print("-" * 40)

    print("Created Array:", array)
    print("-" * 40)

    sorted_array = sorted(array)
    print("Sorted Array:", sorted_array)
    print("-" * 40)

    binary_search(sorted_array, target)


MAIN()
#   ⏱ Time Complexity
# Best Case	O(1)
# Worst Case	O(log n)
# Average	O(log n)
graph-algorithmsdef linear_search(array, x):
    i = 0
    while i < len(array):
        if array[i] == x:
            print("Element found at index", i)
            return
        i += 1
    print("Element not found in the array")
    return

def MAIN():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    x = int(input("Please enter the number to search: "))
    linear_search(array, x)

MAIN()

# Linear Search Time Complexity:
# Best case: O(1) → element is first
# Worst case: O(n) → element is last or not found
# Average case: O(n/2) → element is somewhere in the middle

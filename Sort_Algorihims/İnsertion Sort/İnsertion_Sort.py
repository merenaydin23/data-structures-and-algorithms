def insertion_sort_1(arr):
    step = 0
    i = 0
    j = 1
    while step < len(arr):
        step = step + 1
        a = i
        b = j
        while b > 0 and arr[a] > arr[b]:
            temp = arr[a]
            arr[a] = arr[b]
            arr[b] = temp
            b = b - 1
            a = a - 1

        i = i + 1
        j = j + 1
        if j == len(arr):
            return arr


def insertion_sort_2(A):
    n = len(A)
    for i in range(1, n):
        j = i - 1
        key = A[i]
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A


def Main():
    print("Insertion Sort")
    a = [2, 22, 0, 55, 11, 33, 20, 0, 77, -9, 888, 77]
    b = insertion_sort_1(a)
    print(b)
    c = insertion_sort_2(b)
    print(c)


Main()
# Time Complexity:
#   Best Case: O(n)
#   Average Case: O(n^2)
#   Worst Case: O(n^2)
# Space Complexity: O(1)


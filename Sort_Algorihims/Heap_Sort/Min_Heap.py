def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # sol çocuk daha büyükse
    if left < n and arr[left] < arr[smallest]:
        largest = left

    # sağ çocuk daha büyükse
    if right < n and arr[right] < arr[smallest]:
        largest = right

    # en büyük ebeveyn değilse swap + alt ağacı düzelt
    if largest != i:
        arr[i], arr[largest] = arr[smallest], arr[i]
        heapify(arr, n, largest)



def heap_sort(arr):
    n = len(arr)

    # 1) MAX HEAP OLUŞTUR
    i = n // 2 - 1
    while i >= 0:
        heapify(arr, n, i)
        i -= 1

    # 2) SIRALA
    i = n - 1
    while i > 0:
        arr[i], arr[0] = arr[0], arr[i]    # en büyük sona
        heapify(arr, i, 0)                # kalan kısmı düzelt
        i -= 1


def main():
    arr = [12, 11, 13, 5, 6, 7]
    print("Başlangıç:", arr)

    heap_sort(arr)
    print("Sıralanmış:", arr)


main()

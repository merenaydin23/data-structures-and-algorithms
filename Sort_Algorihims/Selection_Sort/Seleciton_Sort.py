def selection_sort(arr):
    n = len(arr)
    i = 0

    while i < n - 1:
        min_index = i
        j = i + 1

        while j < n:
            if arr[min_index] > arr[j]:
                min_index = j
            j = j + 1

        arr[i], arr[min_index] = arr[min_index], arr[i]
        i = i + 1


if __name__ == "__main__":
    liste = [5, 3, 8, 4, 2]
    print("Başlangıç listesi:", liste)

    selection_sort(liste)

    print("Sıralanmış liste:", liste)


# ------------------------------------------------------------
# 📊 ZAMAN VE ALAN KARMAŞIKLIĞI ANALİZİ:
# En iyi durum (Best Case):    O(n^2)
# Ortalama durum (Average):   O(n^2)
# En kötü durum (Worst Case):  O(n^2)
# Alan karmaşıklığı (Space):  O(1)
# ------------------------------------------------------------

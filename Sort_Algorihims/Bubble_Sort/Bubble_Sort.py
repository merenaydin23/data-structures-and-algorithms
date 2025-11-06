def bubble_sort(arr):
    n = len(arr)
    i = 0

    while i < n - 1:
        swapp = False
        j = 0

        # Her turda en büyük eleman sona taşınır
        while j < n - i - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapp = True
            j += 1

        # Eğer hiç değişim olmadıysa, dizi zaten sıralıdır
        if not swapp:
            break

        i += 1


if __name__ == "__main__":
    liste = [5, 3, 8, 4, 2]
    print("Başlangıç listesi:", liste)

    bubble_sort(liste)
    print("Sıralanmış liste:", liste)


# ------------------------------------------------------------
# 📊 ZAMAN VE ALAN KARMAŞIKLIĞI ANALİZİ:
# En iyi durum (Best Case):    O(n)     -> Liste zaten sıralıysa
# Ortalama durum (Average):   O(n^2)   -> Rastgele karışık liste
# En kötü durum (Worst Case):  O(n^2)   -> Liste tamamen tersse
# Alan karmaşıklığı (Space):  O(1)     -> Ekstra alan kullanılmaz (in-place)
# ------------------------------------------------------------

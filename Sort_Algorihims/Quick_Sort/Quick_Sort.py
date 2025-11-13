def quickSort(arr):
    # Eğer 1 veya 0 eleman varsa zaten sıralı
    if len(arr) <= 1:
        return arr

    # Pivot: ilk eleman
    pivot = arr[0]
    sol = []
    sag = []

    # Pivot'tan küçük ve büyük olanları ayır
    for x in arr[1:]:
        if x < pivot:
            sol.append(x)
        else:
            sag.append(x)

    # Sol ve sağ tarafı sırala, birleştir
    return quickSort(sol) + [pivot] + quickSort(sag)


def main():
    sayilar = [7, 3, 8, 1, 9, 2]
    print("Orijinal dizi:", sayilar)
    sirali = quickSort(sayilar)
    print("Quick Sort ile Sıralanmış dizi:", sirali)


# Programın başlangıç noktası
if __name__ == "__main__":
    main()


# 🕒 Zaman Karmaşıklığı:
# En iyi durum (Best Case): O(n log n)
# Ortalama durum (Average Case): O(n log n)
# En kötü durum (Worst Case): O(n²)

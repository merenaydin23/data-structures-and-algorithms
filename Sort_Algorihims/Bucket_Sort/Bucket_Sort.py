def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bucket_sort(liste):
    bucket_count = 8
    buckets = [[] for _ in range(bucket_count)]
    min_value = min(liste)
    max_value = max(liste)
    interval = (max_value - min_value + 1) / len(buckets)

    # 🔹 Elemanları kovalarına yerleştir
    for a in liste:
        index = int((a - min_value) / interval)
        if index == bucket_count:  # son kova için
            index -= 1
        buckets[index].append(a)

    # 🔹 Kovaları göster (sıralama öncesi)
    print("Kovalar (Sıralama Öncesi):")
    for i, a in enumerate(buckets):
        print(f"Kova {i}: {a}")

    # 🔹 Her kovayı sırala
    for a in buckets:
        insertion_sort(a)

    # 🔹 Kovaları birleştir
    new_list = []
    for a in buckets:
        new_list.extend(a)

    # 🔹 Sıralı sonucu göster
    print("\nKovalar (Sıralama Sonrası):")
    for i, a in enumerate(buckets):
        print(f"Kova {i}: {a}")

    print("\nTam Sıralı Liste:", new_list)
    return new_list


# 🧠 Main kısmı
if __name__ == "__main__":
    liste = [119, -3, 210, 44, 289, 142, 302, 28, -9, 230, 176, 12, 321, 67, 59, 188, 99, 0, 103, 265, 155, 85]
    print("Orijinal Liste:", liste)
    print("\n")
    bucket_sort(liste)
# 🪣 Bucket Sort Zaman Karmaşıklıkları

# En iyi durum (Best Case): O(n + k)
# - Elemanlar kovalar arasında eşit dağılmıştır.
# - Kovalar neredeyse sıralıdır, bu yüzden iç sıralama çok az işlem gerektirir.
# - Toplam süre giriş boyutu (n) ve kova sayısına (k) bağlı olarak neredeyse doğrusal olur.

# Ortalama durum (Average Case): O(n + k)
# - Elemanların kovalar arasında dengeli bir şekilde dağıldığı varsayılır.
# - Kovalar küçük alt listelerdir ve genellikle insertion sort ile sıralanır.
# - Bu durumda da süre yaklaşık olarak O(n + k) olur.

# En kötü durum (Worst Case): O(n^2)
# - Tüm elemanlar tek bir kovaya düşerse, kovada n eleman sıralanmak zorunda kalır.
# - Kullanılan alt sıralama algoritması (örneğin insertion sort) nedeniyle karmaşıklık O(n^2) olur.

# Özet:
# Best Case   -> O(n + k)
# Average Case -> O(n + k)
# Worst Case   -> O(n^2)

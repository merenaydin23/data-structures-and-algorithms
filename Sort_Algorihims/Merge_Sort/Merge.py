def mergeSort(dizi):
    if len(dizi) <= 1:
        return

    orta = len(dizi) // 2
    sol = []
    sağ = []

    i = 0
    while i < orta:
        sol.append(dizi[i])
        i += 1

    i = orta
    while i < len(dizi):
        sağ.append(dizi[i])
        i += 1

    mergeSort(sol)
    mergeSort(sağ)
    merge(dizi, sol, sağ)


def merge(dizi, sol, sağ):
    i, j, k = 0, 0, 0

    while i < len(sol) and j < len(sağ):
        if sol[i] < sağ[j]:
            dizi[k] = sol[i]
            i += 1
        else:
            dizi[k] = sağ[j]
            j += 1
        k += 1

    while i < len(sol):
        dizi[k] = sol[i]
        i += 1
        k += 1

    while j < len(sağ):
        dizi[k] = sağ[j]
        j += 1
        k += 1


# 🧩 Ana program
if __name__ == "__main__":
    sayilar = [5, 4, 0, 2, 3, 8, 9]
    mergeSort(sayilar)
    print("Sıralı dizi:", sayilar)

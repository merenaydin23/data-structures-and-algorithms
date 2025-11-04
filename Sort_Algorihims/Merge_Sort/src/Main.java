public class Main {
    public static void main(String[] args) {
        int[] sayilar = {5, 4, 0, 2, 3, 8, 9};
        MergeSort(sayilar);

        System.out.print("Sıralı dizi: ");
        for (int s : sayilar)
            System.out.print(s + " ");
    }

    public static void MergeSort(int[] dizi) {
        if (dizi.length <= 1)
            return;

        int orta = dizi.length / 2;
        int[] sol = new int[orta];
        int[] sağ = new int[dizi.length - orta];

        for (int i = 0; i < orta; i++) {
            sol[i] = dizi[i];
        }

        for (int i = orta; i < dizi.length; i++) {
            sağ[i - orta] = dizi[i];
        }

        MergeSort(sağ);
        Merge(dizi, sol, sağ);
    }

    public static void Merge(int[] dizi, int[] sol, int[] sağ) {
        int i = 0, j = 0, k = 0; // i sol dizinin indeksi ,j sağ dizi indeksi,k ana dizi indeksi

        while (i < sol.length && j < sağ.length) {
            if (sol[i] <= sağ[j]) {
                dizi[k] = sol[i];
                i++;
            } else {
                dizi[k] = sağ[j];
                j++;
            }
            k++;
        }

        while (i < sol.length) {
            dizi[k] = sol[i];
            i++;
            k++;
        }

        while (j < sağ.length) {
            dizi[k] = sağ[j];
            j++;
            k++;
        }
    }
}

/*
-------------------------------
🔹 Merge Sort Zaman Analizi 🔹
-------------------------------

➡️ En iyi durum (Best Case):
   Dizi zaten sıralı olsa bile Merge Sort yine bölme ve birleştirme işlemlerini yapar.
   Zaman karmaşıklığı: O(n log n)

➡️ Ortalama durum (Average Case):
   Rastgele karışık bir dizide de aynı işlemler gerçekleşir.
   Zaman karmaşıklığı: O(n log n)

➡️ En kötü durum (Worst Case):
   Dizi tamamen ters sıralı olsa bile Merge Sort yine aynı sayıda işlem yapar.
   Zaman karmaşıklığı: O(n log n)

➡️ Ek bilgi:
   - Bellek karmaşıklığı (Space Complexity): O(n)
     Çünkü geçici olarak "sol" ve "sağ" dizileri oluşturulur.
   - Merge Sort’un avantajı: Kararlı (stable) bir sıralama algoritmasıdır.
   - Dezavantajı: Ekstra bellek kullanır.
*/

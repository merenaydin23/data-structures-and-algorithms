public class MergeSortAdimAdim {

    public static void mergeSort(int[] dizi) {
        // 1️⃣ Eğer dizide 1 veya 0 eleman varsa, zaten sıralı
        if (dizi.length <= 1) {
            return;
        }

        // 2️⃣ Diziyi ortadan ikiye böl
        int orta = dizi.length / 2;
        int[] sol = new int[orta];
        int[] sag = new int[dizi.length - orta];

        // 3️⃣ Sol kısmı doldur
        for (int i = 0; i < orta; i++) {
            sol[i] = dizi[i];
        }

        // 4️⃣ Sağ kısmı doldur
        for (int i = orta; i < dizi.length; i++) {
            sag[i - orta] = dizi[i];
        }

        // 🧠 ŞU AN BÖLÜYORUZ
        System.out.print("Bölünüyor: ");
        yazdir(dizi);

        // 5️⃣ Sol tarafı sırala
        mergeSort(sol);
        // 6️⃣ Sağ tarafı sırala
        mergeSort(sag);

        // 7️⃣ Şimdi iki tarafı birleştir
        merge(dizi, sol, sag);

        // 🧩 BİRLEŞTİRİLDİKTEN SONRA
        System.out.print("Birleşti: ");
        yazdir(dizi);
    }

    public static void merge(int[] dizi, int[] sol, int[] sag) {
        int i = 0, j = 0, k = 0;

        // Karşılaştır ve sırayla diziye koy
        while (i < sol.length && j < sag.length) {
            if (sol[i] < sag[j]) {
                dizi[k++] = sol[i++];
            } else {
                dizi[k++] = sag[j++];
            }
        }

        // Sol dizide kalan elemanları ekle
        while (i < sol.length) {
            dizi[k++] = sol[i++];
        }

        // Sağ dizide kalan elemanları ekle
        while (j < sag.length) {
            dizi[k++] = sag[j++];
        }
    }

    // 👇 Diziyi ekrana düzgün basmak için yardımcı metot
    public static void yazdir(int[] dizi) {
        System.out.print("[");
        for (int i = 0; i < dizi.length; i++) {
            System.out.print(dizi[i]);
            if (i < dizi.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }

    public static void main(String[] args) {
        int[] sayilar = {5, 4, 0, 2, 3, 8, 9};

        System.out.print("Başlangıç: ");
        yazdir(sayilar);

        mergeSort(sayilar);

        System.out.print("Sonuç: ");
        yazdir(sayilar);
    }
}

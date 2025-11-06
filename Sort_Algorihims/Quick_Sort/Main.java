import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Başlangıçta sıralanacak liste
        List<Integer> liste = Arrays.asList(10, 5, 8, 3, 15, 12);
        System.out.println("Orijinal Liste: " + liste);

        // Quick Sort fonksiyonunu çağır ve sonucu al
        List<Integer> sirali = quickSort(liste);
        System.out.println("Quick Sort ile Sıralanmış Liste: " + sirali);
    }

    public static List<Integer> quickSort(List<Integer> liste) {
        // Eğer listedeki eleman sayısı 1 veya daha azsa, zaten sıralıdır
        if (liste.size() <= 1) {
            return liste;
        }

        // Pivot eleman olarak ilk elemanı seçiyoruz
        int pivot = liste.get(0);

        // Pivot’tan küçük ve büyük elemanlar için iki yeni liste
        List<Integer> sol = new ArrayList<>();
        List<Integer> sag = new ArrayList<>();

        // Listedeki diğer elemanları pivot’a göre ayır
        for (int i = 1; i < liste.size(); i++) {
            if (liste.get(i) < pivot) {
                sol.add(liste.get(i)); // Pivot’tan küçükler
            } else {
                sag.add(liste.get(i)); // Pivot’tan büyük veya eşit olanlar
            }
        }

        // Sonucu birleştir: önce sol, sonra pivot, sonra sağ
        List<Integer> sonuc = new ArrayList<>();
        sonuc.addAll(quickSort(sol));
        sonuc.add(pivot);
        sonuc.addAll(quickSort(sag));

        return sonuc;
    }
}

// 🕒 Zaman Karmaşıklığı:
// En iyi durum: O(n log n)
// Ortalama durum: O(n log n)
// En kötü durum: O(n²)

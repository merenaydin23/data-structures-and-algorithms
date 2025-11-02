public class Main {
    public static void main(String[] args) {
        int[] c = {101, 20, 5, 22, 11, 0, 99, -9, 55, -66, 909, 100};

        insertion_Sort(c);

        System.out.println("Sıralama sonrası:");
        for (int num : c) {
            System.out.print(num + " ");
        }
    }

    public static void insertion_Sort(int[] a) {
        int n = a.length;
        for (int i = 1; i < n; i++) {
            int key = a[i];
            int j = i - 1;

            // key'den büyük elemanları sağa kaydır
            while (j >= 0 && a[j] > key) {
                a[j + 1] = a[j];
                j = j - 1;
            }

            a[j + 1] = key;
        }
    }
}

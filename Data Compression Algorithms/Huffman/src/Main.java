import java.util.*;

public class Main {
    public static void main(String[] args) {

        // Başlangıç karakterleri ve frekansları
        List<Node> C = new ArrayList<>();
        C.add(new Node('a',45));
        C.add(new Node('b',13));
        C.add(new Node('c',12));
        C.add(new Node('d',16));
        C.add(new Node('e',9));
        C.add(new Node('f',5));

        // Huffman ağacını oluştur
        Node root = Node.huffman(C);

        // Huffman kodlarını yazdır
        System.out.println("Huffman Kodları:");
        Node.printCodes(root, "");
    }

    public static class Node{
        char symbol;
        int freq ;
        Node left,right;

        Node(char symbol,int freg){  // Yaprak düğüm
            this.symbol = symbol;
            this.freq = freg;
            left = right = null;
        }

        Node(int freq){              // İç düğüm
            this.symbol = '\0';
            this.freq = freq;
            left = right = null;
        }

        static Node huffman(List<Node> C){
            List<Node> Q = new ArrayList<>(C);
            int n = Q.size();

            for (int i = 1 ; i < n; i++){
                Node z = new Node(0);

                Node x = extractMin(Q);
                Node y = extractMin(Q);

                z.freq = x.freq + y.freq ;
                z.left = x ;
                z.right = y;

                Q.add(z);
            }
            return extractMin(Q);
        }

        static Node extractMin(List<Node> Q) {
            Node min = Q.get(0);

            for (int i = 0; i < Q.size(); i++) {
                Node node = Q.get(i);
                if (node.freq < min.freq) {
                    min = node;
                }
            }
            Q.remove(min);
            return min;
        }

        static void printCodes(Node root, String code) {
            if(root == null) return;

            if (root.left == null && root.right == null) {
                System.out.println(root.symbol + " : " + code);
                return;
            }

            printCodes(root.left, code + "0");
            printCodes(root.right, code + "1");
        }
    }
}

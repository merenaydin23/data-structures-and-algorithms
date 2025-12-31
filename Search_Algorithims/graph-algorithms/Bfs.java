import java.util.LinkedList;
import java.util.Queue;

public class Bfs {

    static class Graph {
        int V; // Düğüm sayısı
        LinkedList<Integer>[] adj;

        // Constructor
        Graph(int V) {
            this.V = V;
            adj = new LinkedList[V];

            for (int i = 0; i < V; i++) {
                adj[i] = new LinkedList<>();
            }
        }

        // Kenar ekleme (Undirected Graph)
        void addEdge(int u, int v) {
            adj[u].add(v);
            adj[v].add(u);
        }

        // BFS Algoritması
        void bfs(int s) {
            String[] color = new String[V];
            int[] distance = new int[V];
            int[] parent = new int[V];

            // Initialization
            for (int i = 0; i < V; i++) {
                color[i] = "WHITE";
                distance[i] = Integer.MAX_VALUE;
                parent[i] = -1;
            }

            color[s] = "GRAY";
            distance[s] = 0;

            Queue<Integer> queue = new LinkedList<>();
            queue.add(s);

            while (!queue.isEmpty()) {
                int u = queue.poll();

                for (int v : adj[u]) {
                    if (color[v].equals("WHITE")) {
                        color[v] = "GRAY";
                        distance[v] = distance[u] + 1;
                        parent[v] = u;
                        queue.add(v);
                    }
                }

                color[u] = "BLACK";
            }

            // Sonuçları yazdır
            System.out.println("BFS Sonuçları:");
            for (int i = 0; i < V; i++) {
                System.out.println(
                        "Düğüm: " + i +
                                " | Mesafe: " + distance[i] +
                                " | Parent: " + parent[i]
                );
            }
        }
    }

    // MAIN
    public static void main(String[] args) {

        Graph graph = new Graph(6);

        graph.addEdge(0, 1);
        graph.addEdge(0, 2);
        graph.addEdge(1, 3);
        graph.addEdge(1, 4);
        graph.addEdge(2, 5);

        graph.bfs(0);
    }
}

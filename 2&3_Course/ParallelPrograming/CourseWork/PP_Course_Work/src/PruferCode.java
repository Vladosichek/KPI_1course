import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class PruferCode {

    public static int[][] pruferCode2Graph(int[] pruferCode) {
        int n = pruferCode.length + 2;
        int[][] graph = new int[n][n];
        int[] degree = new int[n];
        Arrays.fill(degree, 1);
        for (int v : pruferCode)
            ++degree[v];
        int ptr = 0;
        while (degree[ptr] != 1)
            ++ptr;
        int leaf = ptr;
        for (int v : pruferCode) {
            graph[leaf][v] = 1;
            graph[v][leaf] = 1;
            --degree[leaf];
            --degree[v];
            if (degree[v] == 1 && v < ptr) {
                leaf = v;
            } else {
                for (++ptr; ptr < n && degree[ptr] != 1; ++ptr);
                leaf = ptr;
            }
        }
        for (int v = 0; v < n - 1; v++) {
            if (degree[v] == 1) {
                graph[v][n - 1] = 1;
                graph[n - 1][v] = 1;
            }
        }
        return graph;
    }

    public static int[] graph2PruferCode(int[][] graph) {
        int n = graph.length;
        int[] res = new int[n - 2];
        int[] degrees = new int[n];

        // Calculate degrees of vertices
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 1) {
                    degrees[i]++;
                }
            }
        }

        for (int k = 0; k < n - 2; k++) {
            int leaf = -1;
            // Find a leaf vertex
            for (int i = 0; i < n; i++) {
                if (degrees[i] == 1) {
                    leaf = i;
                    break;
                }
            }

            int neighbor = -1;
            // Find a neighbor of the leaf
            for (int j = 0; j < n; j++) {
                if (graph[leaf][j] == 1) {
                    neighbor = j;
                    break;
                }
            }

            res[k] = neighbor;
            // Update degrees and remove the edge
            degrees[neighbor]--;
            degrees[leaf]--;
            graph[leaf][neighbor] = 0;
            graph[neighbor][leaf] = 0;
        }
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the quantity of nodes in graph: ");
        int n = sc.nextInt();
        int[] code = new int[n - 2];
        Random random = new Random();
        for (int i = 0; i < n - 2; i++) {
            code[i] = random.nextInt(n);
        }
        System.out.println("Prufer code generated!");
        System.out.println("Prufer code: " + Arrays.toString(code));

        int[][] graph = pruferCode2Graph(code);
        System.out.println("Tree represented as adjacency matrix:");
        for (int[] row : graph) {
            System.out.println(Arrays.toString(row));
        }
        long startTime = System.nanoTime();
        int[] ncode = graph2PruferCode(graph);
        long endTime = System.nanoTime();
        System.out.println("Generated Prufer code from tree: " + Arrays.toString(ncode));
        long duration = (endTime - startTime);
        System.out.println("Time of execution: " + duration + " ns");
        boolean flag = true;
        for (int i = 0; i < n - 2; i++) {
            if (code[i] != ncode[i]) {
                flag = false;
                break;
            }
        }
        if (flag) {
            System.out.println("Prufer code is correct!");
        } else {
            System.out.println("Prufer code is incorrect!");
        }
        sc.close();
    }
}

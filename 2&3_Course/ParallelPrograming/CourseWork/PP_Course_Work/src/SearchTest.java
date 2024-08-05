import java.util.Arrays;
import java.util.Random;
import java.util.concurrent.*;

public class SearchTest {

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

    static class SearchTask extends RecursiveTask<Integer> {
        private final int[] array;
        private final int start;
        private final int end;
        private final int threshold = 1000;

        SearchTask(int[] array, int start, int end) {
            this.array = array;
            this.start = start;
            this.end = end;
        }

        @Override
        protected Integer compute() {
            if (end - start <= threshold) {
                for (int i = start; i < end; i++) {
                    if (array[i] == 1) {
                        return i;
                    }
                }
                return -1;
            } else {
                int mid = (start + end) / 2;
                SearchTask leftTask = new SearchTask(array, start, mid);
                SearchTask rightTask = new SearchTask(array, mid, end);

                leftTask.fork();
                int rightResult = rightTask.compute();
                int leftResult = leftTask.join();

                return (leftResult != -1) ? leftResult : rightResult;
            }
        }
    }

    public static int parallelSearch(int[] array) {
        ForkJoinPool pool = new ForkJoinPool(8);
        return pool.invoke(new SearchTask(array, 0, array.length));
    }



    public static void main(String[] args) throws ExecutionException, InterruptedException{
        int n = 30000;
        int[] code = new int[n - 2];
        Random random = new Random();
        for (int i = 0; i < n - 2; i++) {
            code[i] = random.nextInt(n);
        }
        System.out.println("Prufer code generated!");

        int[][] graph = pruferCode2Graph(code);
        int[] degrees = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 1) {
                    degrees[i]++;
                }
            }
        }
        long startTime = System.nanoTime();
        int leaf = -1;
        for (int i = 0; i < n; i++) {
            if (degrees[i] == 1) {
                leaf = i;
            }
        }
        long endTime = System.nanoTime();
        long duration = (endTime - startTime);
        System.out.println("Time of worst sequentional execution: " + duration + " ns");
        for (int i = 0; i < n; i++) {
            if (degrees[i] == 1) {
                leaf = i;
                break;
            }
        }

        long startTimeOne = System.nanoTime();
        int indexOne = parallelSearch(degrees);
        long endTimeOne = System.nanoTime();
        long durationOne = (endTimeOne - startTimeOne);
        System.out.println("Time of parallel execution: " + durationOne + " ns");
        if (leaf == indexOne) {
            System.out.println("Search is correct!");
        } else {
            System.out.println("Search is incorrect!");
        }

    }
}

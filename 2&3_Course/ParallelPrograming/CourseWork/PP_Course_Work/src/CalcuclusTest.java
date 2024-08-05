import java.util.Arrays;
import java.util.Random;
import java.util.concurrent.*;
import java.util.*;
import java.util.stream.IntStream;

public class CalcuclusTest {

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

    public static void main(String[] args) {
        int n = 10000;
        int threads = 8;
        int[] code = new int[n - 2];
        Random random = new Random();
        for (int i = 0; i < n - 2; i++) {
            code[i] = random.nextInt(n);
        }
        System.out.println("Prufer code generated!");

        int[][] graph = pruferCode2Graph(code);
        int[] degrees = new int[n];
        long startTime = System.nanoTime();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 1) {
                    degrees[i]++;
                }
            }
        }
        long endTime = System.nanoTime();
        long duration = (endTime - startTime);
        //System.out.println("Time of sequential execution: " + duration + " ns");

        int[] degreesone = new int[n];
        ExecutorService executor = Executors.newFixedThreadPool(threads);

        long startTimeone = System.nanoTime();
        for (int i = 0; i < graph.length; i++) {
            int rowIndex = i;
            executor.submit(() -> {
                int count = 0;
                for (int j = 0; j < graph[rowIndex].length; j++) {
                    if (graph[rowIndex][j] == 1) {
                        count++;
                    }
                }
                degreesone[rowIndex] = count;
            });
        }

        executor.shutdown();
        try {
            executor.awaitTermination(1, TimeUnit.MINUTES);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        long endTimeone = System.nanoTime();
        long durationone = (endTimeone - startTimeone);
        System.out.println("Time of controlled parallel execution: " + durationone + " ns");
        boolean flag = true;
        for (int i = 0; i < n; i++) {
            if (degreesone[i] != degrees[i]) {
                flag = false;
                break;
            }
        }
        if (flag) {
            System.out.println("Degrees for code is correct!");
        } else {
            System.out.println("Degrees for code is incorrect!");
        }

        int[] degreestwo = new int[n];
        ExecutorService executortwo = Executors.newFixedThreadPool(threads);
        List<Future<Integer>> futures = new ArrayList<>();
        long startTimetwo = System.nanoTime();
        for (int i = 0; i < graph.length; i++) {
            int rowIndex = i;
            Future<Integer> future = executortwo.submit(() -> {
                int count = 0;
                for (int j = 0; j < graph[rowIndex].length; j++) {
                    if (graph[rowIndex][j] == 1) {
                        count++;
                    }
                }
                return count;
            });
            futures.add(future);
        }

        executortwo.shutdown();

        try {
            for (int i = 0; i < futures.size(); i++) {
                degreestwo[i] = futures.get(i).get();
            }
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
        long endTimetwo = System.nanoTime();
        long durationtwo = (endTimetwo - startTimetwo);
        System.out.println("Time of parallel execution: " + durationtwo + " ns");
        boolean flagtwo = true;
        for (int i = 0; i < n; i++) {
            if (degreestwo[i] != degrees[i]) {
                flagtwo = false;
                break;
            }
        }
        if (flagtwo) {
            System.out.println("Degrees for code is correct!");
        } else {
            System.out.println("Degrees for code is incorrect!");
        }

        int[] degreesfour = new int[n];
        long startTimefour = System.nanoTime();
        IntStream.range(0, n).parallel().forEach(i -> {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 1) {
                    degreesfour[i]++;
                }
            }
        });
        long endTimefour = System.nanoTime();
        long durationfour = (endTimefour - startTimefour);
        System.out.println("Time of simple parallel execution: " + durationfour + " ns");
        boolean flagfour = true;
        for (int i = 0; i < n; i++) {
            if (degreesfour[i] != degrees[i]) {
                flagfour = false;
                break;
            }
        }
        if (flagfour) {
            System.out.println("Degrees for code is correct!");
        } else {
            System.out.println("Degrees for code is incorrect!");
        }

    }
}

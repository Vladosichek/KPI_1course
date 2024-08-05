package org.example.task2;

import java.util.Random;

public class MatrixMultiplicationExperiment {

    private static int[][] generateRandomMatrix(int rows, int cols) {
        Random random = new Random();
        int[][] matrix = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int randomInt = random.nextInt(5) + 1; // Генеруємо випадкове ціле число від 1 до 5
                matrix[i][j] = randomInt; // Присвоюємо це ціле число як частину дійсного числа
            }
        }
        return matrix;
    }


    private static long measureExecutionTime(Runnable task) {
        long startTime = System.nanoTime();
        task.run();
        long endTime = System.nanoTime();
        return endTime - startTime;
    }
    public static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        final int[] dimensions = {50,500,1000,1500};
        final int numThreads = Runtime.getRuntime().availableProcessors();

        for (int dim : dimensions) {
            int[][] matrixA = generateRandomMatrix(dim, dim);
            int[][] matrixC = matrixA;
            int[][] matrixB = generateRandomMatrix(dim, dim);
            int[][] matrixD = matrixB;
            long ForkTime = measureExecutionTime(() -> {
                int[][] result1 = ForkFoxMatrixMultiplier.multiply2(matrixA, matrixB, 5,8);
            });
            long foxTime = measureExecutionTime(() -> {
                int[][] result = FoxMatrixMultiplier.multiply2(matrixC, matrixD, 5, 8);
            });

            System.out.println("Matrix Dimension: " + dim);
            System.out.println("Fork Fox Algorithm Time: " + ForkTime / 1_000_000 + "ms");
            System.out.println("Fox Algorithm Time: " + foxTime / 1_000_000 + "ms");
            System.out.println();
        }

    }
}
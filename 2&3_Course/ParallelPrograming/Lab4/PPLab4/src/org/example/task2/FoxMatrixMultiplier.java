package org.example.task2;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

class FoxMatrixMultiplier {
    private static class Result {
        private final int[][] matrix;
        private final int rowOffset;
        private final int colOffset;

        public Result(int[][] matrix, int rowOffset, int colOffset) {
            this.matrix = matrix;
            this.rowOffset = rowOffset;
            this.colOffset = colOffset;
        }

        public int[][] getMatrix() {
            return matrix;
        }

        public int getRowOffset() {
            return rowOffset;
        }

        public int getColOffset() {
            return colOffset;
        }
    }

    private static class MatrixMultiplicationTask implements Callable<Result> {
        private final int[][] matrixA;
        private final int[][] matrixB;
        private final int rowOffset;
        private final int colOffset;
        private final int k;
        private final int blockSize;

        public MatrixMultiplicationTask(int[][] matrixA, int[][] matrixB, int rowOffset, int colOffset, int k, int blockSize) {
            this.matrixA = matrixA;
            this.matrixB = matrixB;
            this.rowOffset = rowOffset;
            this.colOffset = colOffset;
            this.k = k;
            this.blockSize = blockSize;
        }

        @Override
        public Result call() {
            int[][] result = new int[blockSize][blockSize];
            for (int i = 0; i < blockSize; i++) {
                for (int j = 0; j < blockSize; j++) {
                    for (int x = 0; x < blockSize; x++) {
                        result[i][j] += matrixA[rowOffset + i][k + x] * matrixB[k + x][colOffset + j];
                    }
                }
            }
            return new Result(result, rowOffset, colOffset);
        }
    }

    public static int[][] multiply2(int[][] matrixA, int[][] matrixB, int blockSize, int numThreads) {
        ExecutorService executor = Executors.newFixedThreadPool(numThreads);
        int[][] result = new int[matrixA.length][matrixB[0].length];
        try {
            for (int i = 0; i < matrixA.length; i += blockSize) {
                for (int j = 0; j < matrixB[0].length; j += blockSize) {
                    List<Future<Result>> futures = new ArrayList<>();
                    for (int k = 0; k < matrixA[0].length; k += blockSize) {
                        futures.add(executor.submit(new MatrixMultiplicationTask(matrixA, matrixB, i, j, k, blockSize)));
                    }
                    for (Future<Result> future : futures) {
                        Result res = future.get();
                        for (int x = 0; x < blockSize; x++) {
                            for (int y = 0; y < blockSize; y++) {
                                result[res.getRowOffset() + x][res.getColOffset() + y] += res.getMatrix()[x][y];
                            }
                        }
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            executor.shutdown();
        }
        return result;
    }
    private static int[][] generateMatrix(int rows, int cols) {
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
    public static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] matrix1 = {
                {23, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };
        int[][] matrix2 = {
                {2, 25, 2},
                {4, 25, 6},
                {2, 25, 29}
        };

        int[][] result = FoxMatrixMultiplier.multiply2(matrix1, matrix2, 1, 4);
        printMatrix(result);
    }
}
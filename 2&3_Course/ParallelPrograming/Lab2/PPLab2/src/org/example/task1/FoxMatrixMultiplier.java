package org.example.task1;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

class FoxMatrixMultiplier {
    // Вкладений клас для зберігання результату множення матриці
    private static class Result {
        private final int[][] matrix; // Результуюча матриця
        private final int rowOffset; // Зсув за рядками
        private final int colOffset; // Зсув за стовпцями

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

    // Завдання для виконання множення матриці на блок
    private static class MatrixMultiplicationTask implements Callable<Result> {
        private final int[][] matrixA; // Перша матриця
        private final int[][] matrixB; // Друга матриця
        private final int rowOffset; // Зсув за рядками
        private final int colOffset; // Зсув за стовпцями
        private final int k; // Індекс блоку
        private final int blockSize; // Розмір блоку

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
            int[][] result = new int[blockSize][blockSize]; // Результуюча матриця
            for (int i = 0; i < blockSize; i++) {
                for (int j = 0; j < blockSize; j++) {
                    for (int x = 0; x < blockSize; x++) {
                        result[i][j] += matrixA[rowOffset + i][k + x] * matrixB[k + x][colOffset + j]; // Множення блоків матриць
                    }
                }
            }
            return new Result(result, rowOffset, colOffset); // Повернення результату разом зі зсувами
        }
    }

    // Метод для множення матриць з використанням алгоритму Фокса та вказаною кількістю потоків
    public static int[][] multiply(int[][] matrixA, int[][] matrixB, int blockSize, int numThreads) {
        ExecutorService executor = Executors.newFixedThreadPool(numThreads); // Створення пула потоків
        int[][] result = new int[matrixA.length][matrixB[0].length]; // Результуюча матриця
        try {
            for (int i = 0; i < matrixA.length; i += blockSize) {
                for (int j = 0; j < matrixB[0].length; j += blockSize) {
                    List<Future<Result>> futures = new ArrayList<>();
                    for (int k = 0; k < matrixA[0].length; k += blockSize) {
                        futures.add(executor.submit(new MatrixMultiplicationTask(matrixA, matrixB, i, j, k, blockSize))); // Відправлення завдань для множення блоків
                    }
                    for (Future<Result> future : futures) {
                        Result res = future.get(); // Отримання результату
                        for (int x = 0; x < blockSize; x++) {
                            for (int y = 0; y < blockSize; y++) {
                                result[res.getRowOffset() + x][res.getColOffset() + y] += res.getMatrix()[x][y]; // Збереження результату
                            }
                        }
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            executor.shutdown(); // Завершення роботи пула потоків
        }
        return result; // Повернення результату
    }

    public static void main(String[] args) {
        int SIZE = 3;
        int[][] testMatrixA = MatrixUtils.generateMatrix(SIZE, SIZE);
        System.out.println("Test Matrix A:");
        MatrixUtils.printMatrix(testMatrixA);
        int[][] testMatrixB = MatrixUtils.generateMatrix(SIZE, SIZE);
        System.out.println("Test Matrix B:");
        MatrixUtils.printMatrix(testMatrixB);
        int[][] testResult = multiply(testMatrixA, testMatrixB, 1, 8);
        System.out.println("Result Matrix:");
        MatrixUtils.printMatrix(testResult);

        int[] dimensions = {500, 1000, 1500, 2000, 2500, 3000};
        for (int size : dimensions) {
            int[][] matrixA = MatrixUtils.generateMatrix(size, size);
            int[][] matrixB = MatrixUtils.generateMatrix(size, size);
            long startTime = System.currentTimeMillis();
            int[][] result = multiply(matrixA, matrixB, 50, 8);
            long endTime = System.currentTimeMillis();
            System.out.println("Matrix size " + size + ": " + (endTime - startTime) + " ms");
        }
    }
}
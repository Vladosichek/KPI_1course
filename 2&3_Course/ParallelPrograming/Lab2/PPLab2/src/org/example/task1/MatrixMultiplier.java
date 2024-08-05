package org.example.task1;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

class MatrixMultiplier {
    // Вкладений клас для зберігання результату множення матриці на визначений рядок
    private static class Result {
        private final int[] row; // Результуючий рядок
        private final int rowIndex; // Індекс рядка у вихідній матриці

        public Result(int[] row, int rowIndex) {
            this.row = row;
            this.rowIndex = rowIndex;
        }

        public int[] getRow() {
            return row;
        }

        public int getRowIndex() {
            return rowIndex;
        }
    }

    // Завдання для виконання множення матриці на визначений рядок
    private static class MatrixMultiplicationTask implements Callable<Result> {
        private final int[][] matrixA; // Перша матриця
        private final int[][] matrixB; // Друга матриця
        private final int rowIndex; // Індекс рядка для обчислення

        public MatrixMultiplicationTask(int[][] matrixA, int[][] matrixB, int rowIndex) {
            this.matrixA = matrixA;
            this.matrixB = matrixB;
            this.rowIndex = rowIndex;
        }

        @Override
        public Result call() {
            // Виконання множення для визначеного рядка
            int[] rowResult = new int[matrixB[0].length]; // Результуючий рядок
            for (int j = 0; j < matrixB[0].length; j++) {
                int sum = 0;
                for (int k = 0; k < matrixA[0].length; k++) {
                    sum += matrixA[rowIndex][k] * matrixB[k][j];
                }
                rowResult[j] = sum; // Збереження результату у рядку
            }
            return new Result(rowResult, rowIndex); // Повернення обчисленого рядка разом з його індексом
        }
    }

    // Метод для множення двох матриць з вказаною кількістю потоків
    public static int[][] multiply(int[][] matrixA, int[][] matrixB, int numThreads) {
        ExecutorService executor = Executors.newFixedThreadPool(numThreads); // Створення пула потоків
        int[][] result = new int[matrixA.length][matrixB[0].length]; // Результуюча матриця
        List<Future<Result>> futures = new ArrayList<>(); // Список для зберігання результатів кожного рядка множення
        try {
            // Відправлення завдань множення для кожного рядка
            for (int i = 0; i < matrixA.length; i++) {
                futures.add(executor.submit(new MatrixMultiplicationTask(matrixA, matrixB, i)));
            }
            // Отримання результатів і заповнення результатуючої матриці
            for (Future<Result> future : futures) {
                Result res = future.get(); // Отримання обчисленого рядка
                result[res.getRowIndex()] = res.getRow(); // Присвоєння рядка відповідному індексу у результуючій матриці
            }
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
        executor.shutdown(); // Завершення роботи сервісу виконавців
        return result; // Повернення результуючої матриці
    }

    public static void main(String[] args) {
        int SIZE = 3;
        int[][] testMatrixA = MatrixUtils.generateMatrix(SIZE, SIZE);
        System.out.println("Test Matrix A:");
        MatrixUtils.printMatrix(testMatrixA);
        int[][] testMatrixB = MatrixUtils.generateMatrix(SIZE, SIZE);
        System.out.println("Test Matrix B:");
        MatrixUtils.printMatrix(testMatrixB);
        int[][] testResult = multiply(testMatrixA, testMatrixB, 8);
        System.out.println("Result Matrix:");
        MatrixUtils.printMatrix(testResult);

        int[] dimensions = {500, 1000, 1500, 2000, 2500, 3000};
        for (int size : dimensions) {
            int[][] matrixA = MatrixUtils.generateMatrix(size, size);
            int[][] matrixB = MatrixUtils.generateMatrix(size, size);
            long startTime = System.currentTimeMillis();
            int[][] result = multiply(matrixA, matrixB, 8);
            long endTime = System.currentTimeMillis();
            System.out.println("Matrix size " + size + ": " + (endTime - startTime) + " ms");
        }
    }
}
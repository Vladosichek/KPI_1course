package org.example.task2;
import java.util.concurrent.Callable;

import java.util.concurrent.RecursiveTask;
import java.util.concurrent.ForkJoinPool;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class ForkFoxMatrixMultiplier {
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

    private static class MatrixMultiplicationTask extends RecursiveTask<Result> {
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
        protected Result compute() {
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
        ForkJoinPool pool = new ForkJoinPool(numThreads);
        int[][] result = new int[matrixA.length][matrixB[0].length];
        try {
            for (int i = 0; i < matrixA.length; i += blockSize) {
                for (int j = 0; j < matrixB[0].length; j += blockSize) {
                    List<MatrixMultiplicationTask> tasks = new ArrayList<>();
                    for (int k = 0; k < matrixA[0].length; k += blockSize) {
                        tasks.add(new MatrixMultiplicationTask(matrixA, matrixB, i, j, k, blockSize));
                    }

                    List<Callable<Result>> callableTasks = tasks.stream().map(task -> (Callable<Result>) task::compute).collect(Collectors.toList());

                    List<Result> results = pool.invokeAll(callableTasks).stream().map(future -> {
                        try {
                            return future.get();
                        } catch (Exception e) {
                            e.printStackTrace();
                            return null;
                        }
                    }).collect(Collectors.toList());

                    for (Result res : results) {
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
            pool.shutdown();
        }
        return result;
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

        int[][] result = ForkFoxMatrixMultiplier.multiply2(matrix1, matrix2, 1, 4);
        printMatrix(result);
    }

    public static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

}
package org.example.task1;

import java.util.Random;

public class MatrixUtils {
    // Метод для генерації випадкової матриці з вказаною кількістю рядків і стовпців
    public static int[][] generateMatrix(int rows, int cols) {
        Random random = new Random();
        int[][] matrix = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int randomInt = random.nextInt(10) + 1;
                matrix[i][j] = randomInt;
            }
        }
        return matrix;
    }

    // Метод для виведення матриці на екран
    public static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println();
    }
}

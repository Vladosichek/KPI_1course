package org.example;

import mpi.*;

import java.util.Random;

public class Blocking {
    private static final int MASTER = 0;
    private static final int TAG_OFFSET = 0;
    private static final int TAG_ROWS = 1;
    private static final int TAG_MATRIX_A = 2;
    private static final int TAG_MATRIX_B = 3;
    private static final int TAG_RESULT = 4;
    private static final int MATRIX_SIZE = 500;

    public static void main(String[] args) {
        int offset;
        int rows;


        int[] A = new int[MATRIX_SIZE * MATRIX_SIZE];
        int[] B = new int[MATRIX_SIZE * MATRIX_SIZE];
        int[] C = new int[MATRIX_SIZE * MATRIX_SIZE];

        MPI.Init(args);

        int me = MPI.COMM_WORLD.Rank();
        int size = MPI.COMM_WORLD.Size();

        if (size < 2) {
            MPI.COMM_WORLD.Abort(1);
            throw new RuntimeException("Need at least two MPI tasks. Quitting...\n");
        }

        int numWorkers = size - 1;
        if (me == MASTER) {
            System.out.printf("MPI has started with %d tasks.\n", size);

            Random random = new Random();
            for (int i = 0; i < MATRIX_SIZE; i++) {
                for (int j = 0; j < MATRIX_SIZE; j++) {
                    A[MATRIX_SIZE * i + j] = random.nextInt(10);
                }
            }
            for (int i = 0; i < MATRIX_SIZE; i++) {
                for (int j = 0; j < MATRIX_SIZE; j++) {
                    B[MATRIX_SIZE * i + j] = random.nextInt(10);
                }
            }
            //printMatrix(A, "A");
            //printMatrix(B, "B");

            long startTime = System.currentTimeMillis();

            int avgRow = MATRIX_SIZE / numWorkers;
            int extra = MATRIX_SIZE % numWorkers;
            offset = 0;
            for (int dest = 1; dest <= numWorkers; dest++) {
                rows = (dest <= extra) ? avgRow + 1 : avgRow;
                MPI.COMM_WORLD.Send(new int[] { offset * MATRIX_SIZE}, 0, 1, MPI.INT, dest, TAG_OFFSET);
                MPI.COMM_WORLD.Send(new int[] { rows }, 0, 1, MPI.INT, dest, TAG_ROWS);
                MPI.COMM_WORLD.Send(A, offset * MATRIX_SIZE, rows * MATRIX_SIZE, MPI.INT, dest, TAG_MATRIX_A);
                MPI.COMM_WORLD.Send(B, 0, MATRIX_SIZE * MATRIX_SIZE, MPI.INT, dest, TAG_MATRIX_B);
                offset = offset + rows;
            }

            for (int source = 1; source <= numWorkers; source++) {
                int[] offsetBuffer = new int[1];
                MPI.COMM_WORLD.Recv(offsetBuffer, 0, 1, MPI.INT, source, TAG_OFFSET);
                offset = offsetBuffer[0];
                int[] rowsBuffer = new int[1];
                MPI.COMM_WORLD.Recv(rowsBuffer, 0, 1, MPI.INT, source, TAG_ROWS);
                rows = rowsBuffer[0];
                MPI.COMM_WORLD.Recv(C, offset, rows * MATRIX_SIZE, MPI.INT, source, TAG_RESULT);
            }

            System.out.printf("Execution time for matrix %dx%d and %d workers: %dms\n", MATRIX_SIZE, MATRIX_SIZE, numWorkers, System.currentTimeMillis() - startTime);

            //printMatrix(C, "Result");
        } else {
            int[] offsetBuffer = new int[1];
            MPI.COMM_WORLD.Recv(offsetBuffer, 0, 1, MPI.INT, MASTER, TAG_OFFSET);
            offset = offsetBuffer[0];
            int[] rowsBuffer = new int[1];
            MPI.COMM_WORLD.Recv(rowsBuffer, 0, 1, MPI.INT, MASTER, TAG_ROWS);
            rows = rowsBuffer[0];

            MPI.COMM_WORLD.Recv(A, offset, rows * MATRIX_SIZE, MPI.INT, MASTER, TAG_MATRIX_A);
            MPI.COMM_WORLD.Recv(B, 0, MATRIX_SIZE * MATRIX_SIZE, MPI.INT, MASTER, TAG_MATRIX_B);

            // Perform matrix multiplication
            for (int k = 0; k < MATRIX_SIZE; k++) {
                for (int i = 0; i < rows; i++) {
                    C[offset + MATRIX_SIZE * i + k] = 0;
                    for (int j = 0; j < MATRIX_SIZE; j++) {
                        C[offset + MATRIX_SIZE * i + k] += A[offset + MATRIX_SIZE * i + j] * B[MATRIX_SIZE * j + k];
                    }
                }
            }

            MPI.COMM_WORLD.Send(new int[] { offset }, 0, 1, MPI.INT, MASTER, TAG_OFFSET);
            MPI.COMM_WORLD.Send(new int[] { rows }, 0, 1, MPI.INT, MASTER, TAG_ROWS);
            MPI.COMM_WORLD.Send(C, offset, rows * MATRIX_SIZE, MPI.INT, MASTER, TAG_RESULT);
        }

        MPI.Finalize();
    }

    private static void printMatrix(int[] matrix, String name) {
        System.out.printf("Matrix %s:\n", name);
        for (int i = 0; i < MATRIX_SIZE; i++) {
            System.out.println();
            for (int j = 0; j < MATRIX_SIZE; j++)
                System.out.printf("%6d ", matrix[MATRIX_SIZE * i + j]);
        }
        System.out.println("\n" + "*".repeat(10));
    }
}

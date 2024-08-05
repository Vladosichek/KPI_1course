package org.example;

import java.util.Random;
import mpi.*;

public class CollectiveMain {
    public static void main(String[] args) throws MPIException {
        MPI.Init(args);

        int rank = MPI.COMM_WORLD.Rank();
        int size = MPI.COMM_WORLD.Size();

        int n = 100;
        int rowsPerProcess = n / size;

        double[][] A = new double[n][n];
        double[][] B = new double[n][n];
        double[] C = new double[n];
        double[][] localA = new double[rowsPerProcess][n];
        double[][] localB = new double[rowsPerProcess][n];


        if (rank == 0) {
            Random random = new Random();
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    A[i][j] = random.nextInt(100);
                    B[i][j] = random.nextInt(100);
                }
            }
        }

        MPI.COMM_WORLD.Scatter(A, 0, rowsPerProcess * n, MPI.DOUBLE, localA, 0, rowsPerProcess * n, MPI.DOUBLE, 0);
        MPI.COMM_WORLD.Scatter(B, 0, rowsPerProcess * n, MPI.DOUBLE, localB, 0, rowsPerProcess * n, MPI.DOUBLE, 0);

        double[] partialC = new double[rowsPerProcess];

        for (int i = 0; i < rowsPerProcess; i++) {
            double sumA = 0.0;
            double sumB = 0.0;
            for (int j = 0; j < n; j++) {
                sumA += localA[i][j];
                sumB += localB[i][j];
            }
            double avgA = sumA / n;
            double avgB = sumB / n;
            partialC[i] = avgA * avgB;
        }

        MPI.COMM_WORLD.Gather(partialC, 0, rowsPerProcess, MPI.DOUBLE, C, 0, rowsPerProcess, MPI.DOUBLE, 0);

        if (rank == 0) {
            System.out.println("Resulting array C:");
            for (int i = 0; i < n; i++) {
                System.out.println("C[" + i + "] = " + C[i]);
            }
        }

        MPI.Finalize();
    }
}

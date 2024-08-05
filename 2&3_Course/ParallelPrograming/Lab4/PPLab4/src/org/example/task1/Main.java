package org.example.task1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {
    public static void main(String[] args) throws IOException {
        String[] filenames = {"test2.txt","test3.txt","test4.txt"};
        int[] threadCounts = {1, 2, 4, 8};

        for (String filename : filenames) {
            for (int threadCount : threadCounts) {
                String text = new String(Files.readAllBytes(Paths.get("E:\\Install\\Projects\\ParallelPrograming\\Lab4\\PPLab4\\src\\org\\example\\data\\"+filename)));
                String[] words = text.split("\\s+");

                long startTime = System.currentTimeMillis();
                WordStats stats = WordLengthAnalysis.analyze(words, threadCount);
                long endTime = System.currentTimeMillis();

                System.out.println("File: " + filename + ", Threads: " + threadCount +
                        ", Time: " + (endTime - startTime) + " ms, Average word length: " +
                        (double) stats.getTotalLength() / stats.getTotalCount());
            }
        }
    }
}

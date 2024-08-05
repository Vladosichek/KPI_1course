package org.example.task4;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

class Main {
    public static void main(String[] args) throws IOException {
        File[] files = new File("E:\\Install\\Projects\\ParallelPrograming\\Lab4\\PPLab4\\src\\org\\example\\data\\").listFiles();
        assert files != null;
        final String[] keywords = {"lorem" };

        for (File file : files) {
            final String text = Files.readString(file.toPath());
            if (KeywordMatcher.matchesKeywords(keywords, text)) {
                System.out.println("Found matches in file: " + file.getPath());
            }
        }
    }
}

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;

public class Main {

    private static class LengthTask extends RecursiveTask<Integer> {
        private static final int THRESHOLD = 400;
        private final List<String> wordList;
        private final int startIndex;
        private final int endIndex;

        LengthTask(final List<String> wordList, final int startIndex, final int endIndex) {
            this.wordList = wordList;
            this.startIndex = startIndex;
            this.endIndex = endIndex;
        }

        @Override
        protected Integer compute() {
            if (endIndex - startIndex <= THRESHOLD) {
                return computeDirectly();
            } else {
                int middleIndex = (startIndex + endIndex) / 2;
                final LengthTask rightTask = new LengthTask(wordList, middleIndex, endIndex);
                rightTask.fork();
                final LengthTask leftTask = new LengthTask(wordList, startIndex, middleIndex);

                final int leftResult = leftTask.compute();
                final int rightResult = rightTask.join();
                return leftResult + rightResult;
            }
        }

        private int computeDirectly() {
            int totalLength = 0;
            for (int i = startIndex; i < endIndex; i++) {
                totalLength += wordList.get(i).length();
            }
            return totalLength;
        }
    }

    public static void main(String[] args) throws IOException {
        String[] fileNames = {"1.txt", "2.txt"};
        List<String> allWords = new ArrayList<>();
        for (String fileName : fileNames) {
            final List<String> wordsFromFile = Files.readAllLines(Paths.get(fileName));
            allWords.addAll(wordsFromFile);
        }
        final ForkJoinPool forkJoinPool = ForkJoinPool.commonPool();
        final int totalLength = forkJoinPool.invoke(new LengthTask(allWords, 0, allWords.size()));
        double averageWordLength = (double) totalLength / (double) allWords.size();
        System.out.println("Average word length: " + averageWordLength);
    }
}

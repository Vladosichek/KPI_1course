import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.TimeUnit;
import java.util.List;
import java.util.ArrayList;

public class StripeAlgorithmForkJoin {
    private Matrix rightMatrix, leftMatrix;
    private int numOfThreads;
    private Result result;

    public StripeAlgorithmForkJoin (Matrix leftMatrix, Matrix rightMatrix, int numOfThreads)
    {
        this.leftMatrix = leftMatrix;
        this.rightMatrix = rightMatrix;
        this.numOfThreads = Math.min(numOfThreads, leftMatrix.GetNumOfRows());
        this.result = new Result(this.rightMatrix, this.leftMatrix);
    }

    Result getResult() { return result; }

    public void multiply() {
        ForkJoinPool pool = new ForkJoinPool(numOfThreads);
        long startTime = System.nanoTime();

        int chunkSize = (int) Math.ceil((double) leftMatrix.GetNumOfRows() / numOfThreads);
        List<StripeTask> tasks = new ArrayList<>();
        for (int i = 0; i < leftMatrix.GetNumOfRows(); i += chunkSize) {
            int endRow = Math.min(i + chunkSize, leftMatrix.GetNumOfRows());
            tasks.add(new StripeTask(leftMatrix, rightMatrix, result, i, endRow));
        }
        for (StripeTask task : tasks){
            pool.execute(task);
        }

        pool.shutdown();
        try {
            pool.awaitTermination(Long.MAX_VALUE, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        long endTime = System.nanoTime();
        result.setTime((endTime - startTime) / 1e6f);
    }

}


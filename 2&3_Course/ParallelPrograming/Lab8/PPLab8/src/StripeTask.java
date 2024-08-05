import java.util.concurrent.RecursiveAction;


public class StripeTask extends RecursiveAction {
    private Matrix leftMatrix;
    private Matrix rightMatrix;
    private Result result;
    private int startRow;
    private int endRow;

    public StripeTask(Matrix leftMatrix, Matrix rightMatrix, Result result, int startRow, int endRow) {
        this.leftMatrix = leftMatrix;
        this.rightMatrix = rightMatrix;
        this.result = result;
        this.startRow = startRow;
        this.endRow = endRow;
    }

    @Override
    protected void compute() {
        for (int i = startRow; i < endRow; i++) {
            int[] rowResult = new int[rightMatrix.GetNumOfColumns()];
            for (int j = 0; j < rightMatrix.GetNumOfColumns(); j++) {
                int sum = 0;
                for (int k = 0; k < leftMatrix.GetNumOfColumns(); k++) {
                    sum += leftMatrix.GetMatrix()[i][k] * rightMatrix.GetMatrix()[k][j];
                }
                rowResult[j] = sum;
            }
            synchronized (result) {
                result.getResultMatrix().setRow(i, rowResult);
            }
        }
    }
}

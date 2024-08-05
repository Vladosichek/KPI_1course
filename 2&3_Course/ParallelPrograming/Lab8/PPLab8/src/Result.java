public class Result {
    private Matrix rightMatrix, leftMatrix, resultMatrix;
    private float time;

    public Result(Matrix rightMatrix, Matrix leftMatrix){
        this.rightMatrix = rightMatrix;
        this.leftMatrix = leftMatrix;
        resultMatrix = new Matrix(leftMatrix.GetNumOfColumns(), rightMatrix.GetNumOfRows(), false);
    }

    public void setTime(float time) { this.time = time; }
    public float getTime() { return time; }

    public void setResultMatrix(int[][] matrix) { resultMatrix.setMatrix(matrix); }
    public Matrix getResultMatrix() { return resultMatrix; }
}

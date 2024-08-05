import java.io.Serializable;
import java.util.Random;

public class Matrix implements Serializable{
    private final int numOfRows;
    private final int numOfColumns;
    private int[][] matrix;

    public Matrix(int numOfRows, int numOfColumns, boolean Generate){
        this.numOfRows = numOfRows;
        this.numOfColumns = numOfColumns;
        matrix = new int[this.numOfRows][this.numOfColumns];
        Random random = new Random();
        if (Generate){
            for (int i = 0; i < this.numOfRows; i++) {
                for (int j = 0; j < this.numOfColumns; j++) {
                    matrix[i][j] = random.nextInt(10);
                }
            }
        }

    }

    public void setMatrix(int[][] matrix) { this.matrix = matrix; }
    public void setElement(int i, int j, int element){
        matrix[i][j] = element;
    }
    public int GetNumOfRows() { return numOfRows; }
    public int GetNumOfColumns() { return numOfColumns; }
    public int GetElement(int i, int j) { return matrix[i][j]; }
    public int [][] GetMatrix() { return matrix; }
    public int[] GetRow(int i) {
        int[] row = matrix[i];
        int length = row.length;
        int[] reversedRow = new int[length];
        for (int j = 0; j < length; j++) {
            reversedRow[j] = row[length - j - 1];
        }
        return reversedRow;
    }
    public void setRow(int i, int[] row) { System.arraycopy(row, 0, matrix[i], 0, numOfColumns); }
    public int[] GetColumn(int j) {
        int[] column = new int[numOfRows];
        for (int i = 0; i < numOfRows; i++) {
            column[i] = matrix[i][numOfRows - j - 1];
        }
        return column;
    }

    public Matrix GetBlock(int startRow, int endRow, int startColumn, int endColumn) {
        if (startRow < 0 || startRow >= numOfRows || endRow < 0 || endRow > numOfRows ||
                startColumn < 0 || startColumn >= numOfColumns || endColumn < 0 || endColumn > numOfColumns) {
            throw new IllegalArgumentException("Invalid block boundaries");
        }

        int blockRows = endRow - startRow;
        int blockColumns = endColumn - startColumn;
        int[][] block = new int[blockRows][blockColumns];

        for (int i = startRow, blockRow = 0; i < endRow; i++, blockRow++) {
            for (int j = startColumn, blockColumn = 0; j < endColumn; j++, blockColumn++) {
                block[blockRow][blockColumn] = matrix[i][j];
            }
        }

        Matrix Mblock = new Matrix(block.length, block[0].length, false);
        Mblock.setMatrix(block);

        return Mblock;
    }

    public void transformMatrix(){
        int[] firstColumn = this.GetColumn(0);

        for (int i = 0; i < numOfColumns - 1; i++) {
            for (int j = 0; j < numOfRows; j++) {
                matrix[j][i] = matrix[j][i + 1];
            }
        }

        for (int j = 0; j < numOfRows; j++) {
            matrix[j][numOfColumns - 1] = firstColumn[j];
        }
    }

    public void OutputMatrix(){
        for(int i = 0; i < numOfRows; i++){
            for(int j = 0; j < numOfColumns; j++){
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
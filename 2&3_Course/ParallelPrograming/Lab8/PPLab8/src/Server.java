import java.io.*;
import java.net.*;

public class Server {
    private static final boolean OUTPUT = false;
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(5000)) {
            System.out.println("The server is waiting for a connection...");
            Socket socket = serverSocket.accept();
            System.out.println("Client is connected.");

            ObjectOutputStream output = new ObjectOutputStream(socket.getOutputStream());
            ObjectInputStream input = new ObjectInputStream(socket.getInputStream());

            while (true){
                boolean ClientGenerate = input.readBoolean();
                if (ClientGenerate) {
                    try {
                        Matrix matrix1 = (Matrix) input.readObject();
                        Matrix matrix2 = (Matrix) input.readObject();
                        StripeAlgorithmForkJoin stripeAlgorithmFJ = new StripeAlgorithmForkJoin(matrix1, matrix2, 8);
                        stripeAlgorithmFJ.multiply();
                        output.writeObject(stripeAlgorithmFJ.getResult().getResultMatrix());
                        output.flush();
                    } catch (ClassNotFoundException cnfe) {
                        System.out.println("Class not found for read object: " + cnfe.getMessage());
                        cnfe.printStackTrace();
                    }
                }
                else {
                    int mSize = input.readInt();
                    Matrix matrix1 = new Matrix(mSize, mSize, true);
                    Matrix matrix2 = new Matrix(mSize, mSize, true);
                    if (OUTPUT){
                        System.out.println("First Matrix:");
                        matrix1.OutputMatrix();
                        System.out.println("Second Matrix:");
                        matrix2.OutputMatrix();
                    }
                    StripeAlgorithmForkJoin stripeAlgorithmFJ = new StripeAlgorithmForkJoin(matrix1, matrix2, 8);
                    stripeAlgorithmFJ.multiply();
                    output.writeObject(stripeAlgorithmFJ.getResult().getResultMatrix());
                    output.flush();
                }
            }
        } catch (IOException e) {
            System.out.println("I/O error: " + e.getMessage());
        }
    }
}
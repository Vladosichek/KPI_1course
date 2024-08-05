import java.io.*;
import java.net.*;

public class Client {
    private static final boolean ClientGenereate = false;
    private static final boolean OUTPUT = false;
    public static void main(String[] args) {

        try (Socket socket = new Socket("localhost", 5000)) {
            ObjectOutputStream output = new ObjectOutputStream(socket.getOutputStream());
            ObjectInputStream input = new ObjectInputStream(socket.getInputStream());

            BufferedReader consoleInput = new BufferedReader(new InputStreamReader(System.in));
            String userInput;
            double start_time = System.currentTimeMillis();

            while (true) {
                System.out.println("compute/exit:");
                userInput = consoleInput.readLine();

                if ("exit".equalsIgnoreCase(userInput)) {
                    break;
                }
                else {
                    System.out.println("Enter size of matrices:");
                    int mSize = Integer.parseInt(consoleInput.readLine());
                    start_time = System.currentTimeMillis();
                    output.writeBoolean(ClientGenereate);
                    if (ClientGenereate){
                        Matrix matrix1 = new Matrix(mSize, mSize, true);
                        Matrix matrix2 = new Matrix(mSize, mSize, true);
                        if (OUTPUT) {
                            System.out.println("First Matrix:");
                            matrix1.OutputMatrix();
                            System.out.println("Second Matrix:");
                            matrix2.OutputMatrix();
                        }
                        output.writeObject(matrix1);
                        output.writeObject(matrix2);
                    }
                    else {
                        output.writeInt(mSize);
                    }
                    output.flush();
                }

                try {
                    Matrix response = (Matrix) input.readObject();
                    double end_time = System.currentTimeMillis();
                    if (OUTPUT){
                        System.out.println("Received matrix from server:");
                        response.OutputMatrix();
                    }
                    System.out.println("Time: " + (end_time - start_time) / 1000 + " s");
                } catch (ClassNotFoundException e) {
                    System.out.println("Class not found: " + e.getMessage());
                }
            }

        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter a valid integer.");
        } catch (UnknownHostException e) {
            System.out.println("Server not found: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("I/O error: " + e.getMessage());
        }
    }
}

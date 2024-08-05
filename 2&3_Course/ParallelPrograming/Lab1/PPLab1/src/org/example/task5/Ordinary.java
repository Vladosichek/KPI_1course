package org.example.task5;

public class Ordinary  extends Thread{
    private final String symbol;
    public Ordinary(String symbol) {
        this.symbol = symbol;
    }
    public void run() {
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                System.out.print(this.symbol);
            }
            System.out.println();
        }
    }


}
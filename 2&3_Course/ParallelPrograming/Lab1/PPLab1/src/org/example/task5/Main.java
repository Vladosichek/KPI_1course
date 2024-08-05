package org.example.task5;

public class Main {
    public static void main(String[] args) {
//        Ordinary
//        Improved
        Improved thread1 = new Improved("-");
        Improved thread2 = new Improved("|");
        thread1.start();
        thread2.start();

    }
}
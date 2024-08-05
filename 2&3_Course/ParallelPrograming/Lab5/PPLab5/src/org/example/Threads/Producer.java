package org.example.Threads;

import org.example.Systems.Service;

import java.util.Random;


public class Producer extends Thread {
    private final Service service;

    public Producer(Service service) {
        this.service = service;
    }

    @Override
    public void run() {
        var random = new Random();
        var startTime = System.currentTimeMillis();
        long elapsedTime = 0;

        while (elapsedTime < 10_000) {
            this.service.push(random.nextInt(100));

            try {
                Thread.sleep(random.nextInt(15));
            } catch (InterruptedException ignored) {
            }

            elapsedTime = System.currentTimeMillis() - startTime;
        }

        service.isQOpen = false;
    }
}
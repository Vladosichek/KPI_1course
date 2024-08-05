package org.example.Threads;

import org.example.Systems.Service;
import java.util.Random;

public class Consumer extends Thread {
    private final Service service;

    public Consumer(Service service) {
        this.service = service;
    }

    @Override
    public void run() {
        var random = new Random();

        while(service.isQOpen) {
            service.pop();
            try {
                Thread.sleep(random.nextInt(100));
            } catch (InterruptedException ignored) {}

            service.incrementApprovedCount();
        }
    }

}
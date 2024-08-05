package org.example.Threads;

import org.example.Systems.Service;

public class Spectator extends Thread {
    private Service service;

    public Spectator(Service service) {
        this.service = service;
    }

    @Override
    public void run() {
        while(service.isQOpen) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {}

            System.out.println("Queue size: " + service.getCurrentQueueLength()
                    + ", fail probability: " + Math.round(service.calculateRejectedPercentage() * 100.0) / 100.0);
        }
    }
}
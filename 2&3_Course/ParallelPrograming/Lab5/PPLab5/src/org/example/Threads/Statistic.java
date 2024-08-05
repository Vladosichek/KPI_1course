package org.example.Threads;

import org.example.Systems.Service;

public class Statistic extends Thread {
    private final Service service;
    private int sumQueuesLengths;
    private int iteration;

    public Statistic(Service service) {
        this.service = service;
        sumQueuesLengths = iteration = 0;
    }

    @Override
    public void run() {
        while(service.isQOpen) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException ignored) {}

            sumQueuesLengths += service.getCurrentQueueLength();
            iteration++;
        }
    }

    public double getAverageQueueLength() {
        return  sumQueuesLengths / (double)iteration;
    }
}
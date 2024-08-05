package org.example.Systems;

import java.util.ArrayDeque;
import java.util.Queue;

public class Service {
    private final int QUEUE_SIZE = 3;
    private int rejectCounter;
    private int approveCounter;
    private final Queue<Integer> queue;
    public boolean isQOpen;

    public Service() {
        approveCounter = rejectCounter = 0;
        isQOpen = true;
        queue = new ArrayDeque<>();
    }

    public synchronized void push(int item) {
        if(queue.size() >= QUEUE_SIZE) {
            rejectCounter++;
            return;
        }

        queue.add(item);
        notifyAll();
    }

    public synchronized int pop() {
        while(queue.size() == 0) {
            try {
                wait();
            } catch (InterruptedException ignored) {}
        }

        return queue.poll();
    }

    public synchronized void incrementApprovedCount() {
        approveCounter++;
    }

    public double calculateRejectedPercentage() {
        return rejectCounter / (double)(rejectCounter + approveCounter);
    }

    public synchronized int getCurrentQueueLength () {
        return queue.size();
    }
}
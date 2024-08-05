package org.example.Systems;

import org.example.Threads.Consumer;
import org.example.Threads.Producer;
import org.example.Threads.Spectator;
import org.example.Threads.Statistic;

import java.util.concurrent.Callable;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;


public class Initializer implements Callable<double[]> {
    private boolean isSpectated;

    public Initializer(boolean isSpectated) {
        this.isSpectated = isSpectated;
    }

    public double[] call() {
        var executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        var service = new Service();

        var statistic = new Statistic(service);

        // add to pool
        executor.execute(new Consumer(service));
        if (isSpectated)
            executor.execute(new Spectator(service));
        executor.execute(new Producer(service));
        executor.execute(statistic);

        executor.shutdown();

        System.out.println("System is started");

        // wait to finish
        try {
            boolean ok = executor.awaitTermination(30, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return new double[]{service.calculateRejectedPercentage(), statistic.getAverageQueueLength()};
    }
}
package org.example;

import org.example.Systems.Initializer;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Main {

    public static void main(String[] args) throws Exception {
        //task1();
        //task2(5);
        task3();
    }

    public static void task1() {
        var task = new Initializer(false);
        var results = task.call();

        printStatistic(results[0], results[1]);
    }

    public static void task2(int systemInstancesCount) throws Exception {
        var executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        var tasks = new ArrayList<Callable<double[]>>();

        for (int i = 0; i < systemInstancesCount; i++)
            tasks.add(new Initializer(false));

        List<Future<double[]>> resultList = executor.invokeAll(tasks);
        executor.shutdown();

        double totalAveragesMessages = 0, totalPercentages = 0;
        for(var result : resultList) {
            var info = result.get();

            totalAveragesMessages += info[1];
            totalPercentages += info[0];
        }

        printStatistic(totalPercentages / resultList.size(), totalAveragesMessages / resultList.size());
    }

    public static void task3() {
        var task = new Initializer(true);
        var results = task.call();

        printStatistic(results[0], results[1]);
    }

    private static void printStatistic(double failProb, double avgQSize) {
        System.out.println("Fail probability: " + Math.round(failProb * 100.0) / 100.0);
        System.out.println("Avg queue size: " + Math.round(avgQSize * 100.0) / 100.0);
    }
}
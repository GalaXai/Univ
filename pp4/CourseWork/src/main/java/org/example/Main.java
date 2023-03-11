package org.example;

import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Jakub", "Ola", "Kasia", "Kuba");
        Greeter greeter = new Greeter();
        // greet one person
        greeter.greet("One");

        // greet everyone
        System.out.println("Hello evy'one");
        for(String name : names){
            greeter.greet(name);
        }

        // greet woman's
        System.out.println("Hello ly'ds");
        names.stream()
                .filter(name -> name.endsWith("a")) // in python Lambda x: x[-1] = "a"
                .forEach(greeter::greet);
    }
}
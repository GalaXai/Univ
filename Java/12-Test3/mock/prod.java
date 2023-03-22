package mock;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class prod implements Comparable<prod>{
    private String name;
    private float price;

    public prod(String name,float price){
        this.name = name;
        this.price = price;
    }

    public int compareTo(prod other){
        return this.name.compareTo(other.name);
    }

    public static void main(String[] args) {
        prod product = new prod("dddd", 20);
        prod product1 = new prod("bca", 21);
        prod product2 = new prod("a", 123321);
        List<prod> prodList = new ArrayList<prod>();
        prodList.add(product);
        prodList.add(product1);
        prodList.add(product2);
        System.out.println(prodList);
        Collections.sort(prodList);
        System.out.println(prodList);

    }

}

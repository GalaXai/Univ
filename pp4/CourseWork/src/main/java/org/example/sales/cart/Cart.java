package org.example.sales.cart;

import java.util.ArrayList;
import java.util.List;

public class Cart {

    List<CartItem> items;

    public Cart() {
        this.items = new ArrayList<>();
    }

    public static Cart getEmptyCart(){
        return new Cart();
    }

    public void add(CartItem cartItem){
        items.add(cartItem);
    }

    public List<CartItem> getItems() {
        return items;
    }

    public int itemsCount() {
        return items.size();
    }

    public void remove(CartItem cartItem) {
        items.remove(cartItem);
    }


}

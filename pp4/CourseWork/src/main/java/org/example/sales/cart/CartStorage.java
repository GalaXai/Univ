package org.example.sales.cart;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

public class CartStorage {

    Map<String,Cart> carts;

    public CartStorage() {
        this.carts = new HashMap<>();
    }

    public void save(String customerId, Cart cart) {
        carts.put(customerId, cart);
    }

    public Optional<Cart> getBy(String customerId) {
        return Optional.ofNullable(carts.get(customerId));
    }

}

package org.example.sales.cart;

import java.math.BigDecimal;
public class CartItem {

    private final String ProductId;

    private final String name;

    private final BigDecimal price;

    private int quantity;

    public CartItem(String ProductId, String name, BigDecimal price) {
        this.ProductId = ProductId;
        this.name = name;
        this.price = price;
        this.quantity = 1;
    }

    public static CartItem of(String ProductId, String name, BigDecimal price) {
        return new CartItem(ProductId, name, price);
    }

    public BigDecimal getPrice() {
        return price;
    }

    public int getQuantity() {
        return quantity;
    }

    public String getProductId() {
        return ProductId;
    }

    public String getName() {
        return name;
    }
}

package org.example.sales;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.example.sales.offers.Offer;
public class SalesController {
    Sales sales;

    public SalesController(Sales sales) {
        this.sales = sales;
    }

    @GetMapping("api/sales/current_offer")
    public Offer getCurrentOffer() {
        return sales.getCurrentOffer(getCurrentClientId());
    }

    @PostMapping("api/add-to-cart/{productId}")
    public void addToCart(@PathVariable String productId) {
        sales.addToCart(getCurrentClientId(),productId);
    }

    private String getCurrentClientId() {
        // return random number between 0 and 100
        return String.valueOf((int)(Math.random() * 100));
    }
}

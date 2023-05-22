package org.example.sales.offers;

import org.example.sales.cart.Cart;

import java.math.BigDecimal;

public class OfferCalculator {

    public static Offer calculateOffer(Cart cart) {
        BigDecimal total = cart.getItems()
                .stream()
                .map(cartItem -> cartItem.getPrice().multiply(BigDecimal.valueOf(cartItem.getQuantity())))
                .reduce(BigDecimal::add)
                .orElse(BigDecimal.ZERO);
        return Offer.of(total, cart.itemsCount());
    }
}

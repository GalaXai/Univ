package org.example.sales;

import org.example.sales.cart.CartItem;
import org.example.sales.cart.CartStorage;
import org.example.sales.offers.OfferCalculator;
import org.example.sales.product.ProductDetails;
import org.example.sales.product.ProductDetailsProvider;
import org.example.sales.offers.Offer;
import org.example.sales.cart.Cart;
import org.example.sales.product.ProductNotAvailableException;

public class Sales {
    private CartStorage cartStorage;

    private ProductDetailsProvider productDetailsProvider;


    public Sales(CartStorage cartStorage, ProductDetailsProvider productDetailsProvider) {
        this.cartStorage = cartStorage;
        this.productDetailsProvider = productDetailsProvider;
    }


    public Offer getCurrentOffer(String customerId) {
        Cart cart = cartStorage.getBy(customerId)
                .orElse(Cart.getEmptyCart());

        return OfferCalculator.calculateOffer(cart);
    }

    public void addToCart(String customerId, String productId) {
        Cart cart = cartStorage.getBy(customerId)
                    .orElse(Cart.getEmptyCart());

        ProductDetails details = productDetailsProvider.getProductDetails(productId)
                        .orElseThrow(ProductNotAvailableException::new);

        cart.add(CartItem.of(productId,
                details.getName(),
                details.getPrice()));

        cartStorage.save(customerId, cart);
    }
}

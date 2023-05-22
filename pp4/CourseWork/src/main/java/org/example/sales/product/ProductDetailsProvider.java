package org.example.sales.product;


import java.util.Optional;
public class ProductDetailsProvider {

    // change bellow to optional

    public Optional<ProductDetails> getProductDetails(String productId) {
        return Optional.of(new ProductDetails(productId, "Product name", null));
    }
}

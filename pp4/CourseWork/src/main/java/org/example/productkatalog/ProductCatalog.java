package org.example.productkatalog;


import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class ProductCatalog {

    private ProductStorage productStorage;

    public ProductCatalog(ProductStorage productStorage) {
        this.productStorage = productStorage;
    }

    public List<Product> allProducts() {
        return productStorage.allProducts();
    }

    public String addProduct(String name, String desc){
        Product newOne = new Product(
                UUID.randomUUID(),
                name,
                desc);
        productStorage.add(newOne);

        return newOne.getID();
    }


    public Product loadByID(String productID){
        return null;
    }
    public void changePrice(String productID, BigDecimal newPrice){
        Product product = loadByID(productID);
        product.changePrice(newPrice);
    }
    public void assignImage(String productID,String newImage){
        Product product = loadByID(productID);
        product.setImage(newImage);
    }

    public void publishProduct(String productID){
        Product product = loadByID(productID);

        if (product.getImage() == null) {
            throw new ProductCantBePublishedException();
        }

        if (product.getPrice() == null) {
            throw new ProductCantBePublishedException();
        }

        product.setOnline(true);
    }

    public List<Product> allPublicProducts() {
        return productStorage.allPublishedProducts();
    }
}

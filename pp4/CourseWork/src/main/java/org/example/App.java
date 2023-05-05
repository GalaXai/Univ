package org.example;


import org.example.productkatalog.HashMapProductStorage;
import org.example.productkatalog.ProductCatalog;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import java.math.BigDecimal;

@SpringBootApplication
public class App {
    public static void main(String[] args){
        SpringApplication.run(App.class, args);
        System.out.println("Kurwo");
    }



    @Bean
    ProductCatalog createMyProductCatalog() {
        ProductCatalog productCatalog = new ProductCatalog(new HashMapProductStorage());
        String product1 = productCatalog.addProduct("Harry Potter", "tom 2");
        productCatalog.changePrice(product1, BigDecimal.valueOf(20.90));
        productCatalog.assignImage(product1, "foo/image.jpg");
        productCatalog.publishProduct(product1);

        String product2 = productCatalog.addProduct("Harry Potter", "tom 3");
        productCatalog.changePrice(product2, BigDecimal.valueOf(40.90));
        productCatalog.assignImage(product2, "foo/boo/image.jpg");
        productCatalog.publishProduct(product2);
        return productCatalog;
    }
}

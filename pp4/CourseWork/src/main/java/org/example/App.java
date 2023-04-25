package org.example;


import org.example.productkatalog.HashMapProductStorage;
import org.example.productkatalog.ProductCatalog;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class App {
    public static void main(String[] args){
        SpringApplication.run(App.class, args);
    }

    @Bean
    ProductCatalog createNewProductCatalog(){
        return new ProductCatalog(new HashMapProductStorage());
    }
}

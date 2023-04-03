package org.example.productkatalog;

import java.math.BigDecimal;
import java.util.UUID;

public class Product {
    private final String uuid;
    private final String name;
    private final String desc;
    private BigDecimal price;
    private boolean online;

    private String image;

    public Product(UUID uuid,String name, String desc){
        this.uuid = uuid.toString();
        this.name = name;
        this.desc = desc;
    }

    public String getID(){return uuid;}
    public UUID getUUID(){return UUID.fromString(uuid);}

    public void changePrice(BigDecimal newPrice) {
        this.price =  newPrice;
    }

    public BigDecimal getPrice() {
        return price;
    }
    public String getImage(){return image;}

    public void setImage(String image) {
        this.image = image;
    }
    public void setOnline(boolean status){
        this.online = status;
    }
    public boolean getOnline(){return online;}

}

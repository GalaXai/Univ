import java.util.ArrayList;

public class ShoppingList {
    private ArrayList<Product> products = new ArrayList<>();

    public void add(Proudct product){
        this.products.add(product);
    }

    public String toString(){
        String result = "";
        for(Product product: products){
            result += product.getName() + ",";
        }
        return result.substring(0,result.length()-1); // Removes last char ',' from result
    }

    public int total(){
        int total = 0;
        for(Product product: products){
            total+= product.qetQuantity();
        }
        return total;
    }
}

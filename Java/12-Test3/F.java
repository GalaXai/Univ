public class F implements Comparable<F> {
    private String name;
    private int price;

    public F(String n, int p) {
        setName(n);
        setPrice(p);
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public int getPrice() {
        return price;
    }

    @Override
    public int compareTo(F other) {
        return this.price - other.price;
    }
}

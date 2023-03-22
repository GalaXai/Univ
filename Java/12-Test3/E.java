public class E {
    private String name;
    private String surname;
    private int age;
    private int staz;

    public E(String name, String surname, int age, int staz) {
        this.name = name;
        this.surname = surname;
        this.age = age;
        this.staz = staz;
    }

    @Override
    public String toString() {
        String output = "";
        if (age >= 18) {
            output += surname.toUpperCase() + name.substring(0, 1).toUpperCase() + staz;
        } else {
            output += surname + name.substring(0, 1).toString().toLowerCase() + staz;
        }
        return output;
    }
}
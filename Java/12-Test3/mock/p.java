package mock;

public class p {
    private String name;
    private String surname;

    public  p(String name,String surname){
        this.name  = name;
        this.surname = surname;
    }
    @Override
    public String toString(){
        return name.substring(0,1).toUpperCase() + surname.substring(0,1).toUpperCase();
    }
    public static void main(String[] args){
        p p_1 = new p("anna","may");
        System.out.println(p_1);
    }
}
public class Person {
    String personsName;
    int personsHeight; //cm
    int personsWeight; //kg

    public Person(String name){
        personsName = name;
    }

    public Person(String name,int weight,int height){
        personsName = name;
        personsHeight = height;
        personsWeight = weight;
    }

    public void setWeightAndHeight(int weight,int height){
        personsWeight = weight;
        personsHeight = height;
    }

    public double calculateBMI(){
        return personsWeight / ((personsHeight * personsHeight) /10000f);
    }

    public void displayRecord(){
        System.out.println(personsName +" "+ personsHeight +" cm, " + personsWeight + " kg, BMI: " + calculateBMI());
        if (calculateBMI()>24.9f){System.out.println("BMI too high");}
        if (calculateBMI()<24.9f){System.out.println("BMI too low");}
        else {System.out.println("BMI is correct");}
    }
    public static void main(String[] args){
        Person myObj =  new Person("Billy",63,175);
        myObj.displayRecord();
    }
}

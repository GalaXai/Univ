public class Lamp {
    Boolean state = false;


    public void turnOff(){
        state = false;
    }
    public void turnOn(){
        state = true;
    }

    public void displayInfo(){
        if (state){
            System.out.println("The lamp is turned on");
        }else {
            System.out.println("The lamp is turned off");
        }

    }
    public static void main(String[] args){
        Lamp myObj = new Lamp();
        myObj.displayInfo();
        myObj.turnOn();
        myObj.displayInfo();
        myObj.turnOff();
        myObj.displayInfo();
    }
}

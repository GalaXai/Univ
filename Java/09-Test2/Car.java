public class Vehicle {
    private int seats;
    Vehicle(int s){seats = s;}
    public int getSeats(){return seats;}
}



public class Car extends Vehicle{
    private int maxSpeed;
    Car(int seats,int maxSpeed){
        super(seats);
        this.maxSpeed = maxSpeed;
    }
    public int[] spec(){
        return new int[] {this.getSeats(),this.maxSpeed};
    }
}

import java.util.ArrayList;
import java.util.List;

public class InternetDevice {
    String deviceName;
    static List<String> name = new ArrayList<String>(); //TODO lookup
    Boolean connected;
    static int connected_Devices;

    InternetDevice(String Name){
        deviceName = Name;
        name.add(Name);
        connected_Devices +=1;
    }
    public void connect(){
        if (name.contains(deviceName)) {
            connected = true;
        }else {
            connected = true;
            name.add(deviceName);
        }
    }
    public void disconnect(){
        if (name.contains(deviceName)) {
            connected = false;
            name.remove(deviceName);
        }else {
            connected = false;
        }

    }
    public void isConnected(){
        if (connected){
            System.out.println("Devices are connected to the internet");
        }else{
            System.out.println("Devices are not connected to the internet");
        }
    }

    public static void displayConnections(){
        for (String i : name){
            System.out.print(i + ", ");
        }
        System.out.println("Are connected");
    }

    public static void main(String[] args){
        InternetDevice myObj = new InternetDevice("Billy");
        InternetDevice myObj2 = new InternetDevice("Phone");
        InternetDevice myObj3 = new InternetDevice("TV");
        InternetDevice myObj4 = new InternetDevice("Laptop");
        InternetDevice myObj5 = new InternetDevice("Computer");

        InternetDevice.displayConnections();
        myObj4.disconnect();
        myObj5.disconnect();
        InternetDevice.displayConnections();


    }
}

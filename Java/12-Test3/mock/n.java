package mock;

import java.lang.Math;
public class n {
    private int system;
    private String value;

    public n(int system,String value){
        setSystem(system);
        setValue(value);
    }

    public void setSystem(int system) {
        this.system = system;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public int get10(){
        int count = 0;
        for(int i = 0;i<value.length();i++){
            int a = Character.getNumericValue(value.charAt(value.length()-1-i));
            if(a >= system){
                return -1;
            }
            count += (a * Math.pow(system,i));
        }
        return count;

        // or like this
        // try {
        //     return Integer.parseInt(value, system);
        // } catch (NumberFormatException e){
        //     return -1;
        // }
    }
    public static void main(String[] args) {
        // Example usage
        n number = new n(5, "101");
        System.out.println(number.get10());  // Output: 26

        number.setSystem(8);
        number.setValue("10283");
        System.out.println(number.get10());  // Output: -1
    }
}

import java.lang.Math;
public class n {
    private int system;
    private String value;

    public n(int system,String value){
        setSystem(system);
        setValue(value);
    }

    public void setSystem(int system) {
        this.system = system;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public int get10(){
        int count = 0;
        for(int i = 0;i int a = Character.getNumericValue(value.charAt(value.length()-1-i));
        if(a >= system){
            return -1;
        }
        count += (a * Math.pow(system,i));
    }


// or like this
// try {
// return Integer.parseInt(value, system);
// } catch (NumberFormatException e){
// return -1;
// }
}
    public static void main(String[] args) {
// Example usage
        n number = new n(5, "101");
        System.out.println(number.get10()); // Output: 26

        number.setSystem(8);
        number.setValue("10283");
        System.out.println(number.get10()); // Output: -1
    }
}

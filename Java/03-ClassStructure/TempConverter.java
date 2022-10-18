public class TempConverter {
    float kelvin;
    float celsius;
    float fahrenheit;

    public void kelvinTo(float k){
        kelvin = k;
        celsius = k-273.15f;
        fahrenheit = (k-273.15f)*9/5+32;
        System.out.println(kelvin +" Kelvin = " + celsius + "C " + fahrenheit + "F");
    }
    public void celsiusTo(float  c){
        kelvin = c+273.15f;
        celsius = c;
        fahrenheit = c*9/5+32;
        System.out.println(celsius +" Celsius = " + kelvin + "K " + fahrenheit + "F");
    }
    public void fahrenheitTo(float f){
        kelvin = (f-32f)*5/9 +273.15f;
        celsius = (f-32f)*5/9;
        fahrenheit = f;
        System.out.println(fahrenheit +" Fahrenheit = " + celsius + "C " + kelvin +  "K");
    }
    public static void main(String[] args){
        TempConverter myObj = new TempConverter();
        myObj.kelvinTo(100);
        myObj.celsiusTo(100);
        myObj.fahrenheitTo(100);
    }
}

package mock;

import java.util.ArrayList;
public class cites {
    private ArrayList<String> citynames = new ArrayList<String>();


    public cites(String[] citynames){
        this.citynames = new ArrayList<>();
        for(String city :citynames){
            this.citynames.add(city);
        }
    }
    public cites filter(char ch){
        ArrayList<String> f_citynames = new ArrayList<>();
        for(String city : citynames){
            if(city.charAt(0) == ch){
                f_citynames.add(city);
            }
        }
        return new cites(f_citynames.toArray(String[]::new));
    }

    public String Cities(){
        String result = "";
        for(String city:citynames){
            result +=city;
        }
        return result;
    }

    public static void main(String[] args) {
        String [] test = {"Warszawa","Sopot","Kielce","Szczecin"};
        System.out.println(new cites(test).filter('S').Cities());
    }
}

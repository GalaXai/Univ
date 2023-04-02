package mock;

public class Isogram {
    static boolean Isogram(String s){
        for(int j = 0; j<s.length()-1;j++){
            char litera = s.charAt(j);
            for(int i = j+1;i<s.length();i++){
                if(litera == s.charAt(i)){
                    return false;
                }

            }
        }
        return true;
    }
    public static void main(String[] args){
        System.out.println(Isogram("blue water"));
        System.out.println(Isogram("BLUE water"));

    }
}

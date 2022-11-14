public class Alphabet {
    public static boolean isAlphabet(String t){
        for(int i = 0; i<t.length()-1;i++){
            if (t.charAt(i) > t.charAt(i+1)){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args){
        Alphabet Alphabet = new Alphabet();
        Alphabet.isAlphabet("abegsw");
        Alphabet.isAlphabet("abcmhsw");

    }
}

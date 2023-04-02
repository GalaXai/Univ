public class P {
    public static String m(int num) {
        String output = "";
        if (num > 100) {
            for (int i = 0; i < (num / 100); i++) {
                output += "*";
            }
            num -= (num / 100 * 100);
        }
        if (num > 10) {
            for (int i = 0; i < (num / 10); i++) {
                output += "+";
            }
            num -= (num / 10 * 10);
        }
        if (num > 1) {
            for (int i = 0; i < (num / 1); i++) {
                output += "/";
            }
            num -= (num / 1);
        }
        return output;
    }
}

public class L {
    public B[] bol_list;

    public L(B[] bol_list) {
        this.bol_list = bol_list;
    }

    public int m() {
        int count = 0;
        for (int i = 1; i < bol_list.length - 1; i++) {
            if (bol_list[i - 1].getB() != bol_list[i].getB() && bol_list[i + 1].getB() != bol_list[i].getB()) {
                count++;
            }
        }
        return count;
    }
}

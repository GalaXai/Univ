public class N {
    public String word_1;
    public String word_2;

    public N(String w1, String w2) {
        this.word_1 = w1;
        this.word_2 = w2;
    }

    public N swap() {
        return new N(word_2, word_1);
    }

    @Override
    public String toString() {
        return word_1 + word_2;
    }

    public static void main(String[] args) {
        System.out.println(new N("water", "sun"));
        System.out.print(new N("water", "sun").swap());
    }

}

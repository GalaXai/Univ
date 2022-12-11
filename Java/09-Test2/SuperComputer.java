public class Counter1 {
    private int counter;
    Counter1(int c){counter=c;}
    public void add1(){counter++;}
    public int getCounter(){return counter;}
}

public class SuperComputer extends Counter1{

    SuperComputer(int c){
        super(c);
    }

    public void addN(int n) {
        for (int i = 0; i < n; i++) {
            this.add1();
        }
    }
}

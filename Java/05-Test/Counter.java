public class Counter {
    int count = 0;

    public void increase(){count++;}
    public void decrease(){count--;}

    public void increase(int x){count += x;}
    public void decrease(int x){count -= x;}

    public int value(){return count;}

    public static  void main(String[] ags){
        Counter c = new Counter();
        c.value();
        c.increase();
        c.increase();
        c.decrease();
        c.increase(5);
        c.decrease(2);
        c.value();

    }
}

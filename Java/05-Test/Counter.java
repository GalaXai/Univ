public class Counter {
    int count = 0;

    public void increase(){count++;}
    public void increase(int x){count += x;}

    public void decrease(){count--;}
    public void decrease(int x){count -= x;}

    public int value(){return count;}
}

import java.util.ArrayList;

public class Family {

    private ArrayList<Person> ps = new ArrayList<Person>();

    public int adults() {
        int count = 0;
        for (Person p : ps) {
            if (p.getAge() >= 18) {
                count++;
            }
        }
        return count;
    }

    public void add(Person p) {
        ps.add(p);
    }
}

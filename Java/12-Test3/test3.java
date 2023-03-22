import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;

public class test3 {
	static int total=0;
	static String r = ""; 
	
	public static void main(String[] args) {
		HashMap<String, Integer> results = new HashMap<String, Integer>();

		try {
			assert new E("Barbara","April",15,8).toString().equals("aprilb8");
			assert new E("Peter","August",37,4).toString().equals("AUGUSTP4");
			results.put("E", 1);
		} catch (Throwable e) {
			results.put("E", 0);
		}

		try {
			assert P.m(0).equals("");
			assert P.m(52).equals("+++++//");
			assert P.m(206).equals("**//////");
			results.put("P", 1);
		} catch (Throwable e) {
			results.put("P", 0);
		}

		try {
			int[] p1 = {1,2,3,4,5,5,6,7,9,9};
			int[] p2 = {1,2,3,4,5,1,2,3,4,5};
			assert new C(p1).m() == true;
			assert new C(p2).m() == false;
			results.put("C", 1);
		} catch (Throwable e) {
			results.put("C", 0);
		}

		try {
			assert new N("abc","xyz").toString().equals("abcxyz");
			assert new N("abc","xyz").swap().toString().equals("xyzabc");
			results.put("N", 1);
		} catch (Throwable e) {
			results.put("N", 0);
		}

		try {
			B[] a1 = {new B(true),new B(false),new B(true)};
			B[] a2 = {new B(true),new B(false),new B(true),new B(false),new B(true),new B(true),new B(false)};
			assert new L(a1).m() == 1;
			assert new L(a2).m() == 3;
			results.put("L", 1);
		} catch (Throwable e) {
			results.put("L", 0);
		}

		try {
			F m = new F("milk", 3);
			F w = new F("water", 5);
			F s = new F("sugar", 2);
			F[] f = {m,w,s};
			Arrays.sort(f);
			assert f[0].getPrice() == 2;
			assert f[2].getPrice() == 5;
			results.put("F", 1);
		} catch (Throwable e) {
			results.put("F", 0);
		}

		try {
			Pizza p = new Pizza("vegetaian",70);
			p.setPrice();
			assert p.getPrice() == 60f;
			assert p.discount() == 3f;
			assert p.delivery() == 8f;
			assert p.delivery(3) == 11f;
			results.put("Pizza", 1);
		} catch (Throwable e) {
			results.put("Pizza", 0);
		}

		try {
			Person p1 = new Person("A",25);
			Person p2 = new Person("B",25);
			Person p3 = new Person("C",25);
			Person p4 = new Person("D",25);
			Person p5 = new Person("E",17);
			Person p6 = new Person("F",17);
			Family f = new Family();
			f.add(p1);f.add(p2);f.add(p3);f.add(p4);f.add(p5);f.add(p6);
			assert f.adults() == 4;
			results.put("Family", 1);
		} catch (Throwable e) {
			results.put("Family", 0);
		}





		// Display test results
		//results.forEach((k,v)->System.out.print(k+":"+v+" "));
		results.forEach((k,v)->r += k+":"+v+" ");
		r = r.trim();
		System.out.println(r);
		// Save test results to file
		try {
			FileWriter myWriter = new FileWriter("results.txt");
			myWriter.write(r);
			myWriter.close();
		} catch (IOException e){}
		
	}
}



// Class templates
class E {
	E(String name, String surname, int age, int seniority){}
	public String toString(){return "";}
}

class P {
	public static String m(int n){return "";}
}

class C {
	C(int[] p){}
	public boolean m(){return false;}
}

class N {
	String s1,s2;
	N(String s1,String s2){}
	public N swap(){return new N("","");}
	public String toString(){return "";}	
}

class B {
	private boolean b;
	B(boolean b){this.b = b;}
	public boolean getB(){return b;}
}

class L {
	L(B[] b){}
	public int m(){return 0;}
}

class F {
	String name;
	int price;
	F(String n, int p){}
	public String getName(){return "";}
	public void setName(String name){}
	public int getPrice(){return 0;}
	public void setPrice(int price){}	
}

class Pizza extends Food implements Extra {
	int size;
	Pizza(String name, int size){super(name);}
	public void setPrice(){}
	public float discount(){return 0f;}
	public float delivery(){return 0f;}
	public float delivery(int tip){return 0f;}
}

abstract class Food {
	private String name;
	private float price;
	Food(String name){}
	public String getName(){return name;}
	public float getPrice(){return price;}
	public void setPrice(float p){price = p;}
	public abstract void setPrice();
}

interface Extra {
	float discount();
	float delivery();
	float delivery(int tip);
}

class Family {
	public void add(Person p){}
	public int adults(){return 0;}
}

class Person {
    private String name;
    private int age;
    Person(String n, int a){name=n; age=a;}
    public String getName(){return name;}
    public int getAge(){return age;}
}


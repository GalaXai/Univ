public class mock_Person {
    private String name;
    private int age;

    public mock_Person(String name, int age){
        setName(name);
        setAge(age);
    }

    public void setName(String name){this.name = name;}
    public void setAge(int age){this.age = age;}

    public String getName(){return name;}
    public int  getAge(){return age;}

    public boolean isAdult(){
        if (age >= 18){
            return true;
        }else{return false;}
    }
    public String tostring(){
        return name + "," + age;
    }
    public static void main(String[] args){
        mock_Person p = new mock_Person("Anna",21);
        p.getAge();//=> 21
        p.isAdult(); //=> true
        p.setAge(17);
        p.isAdult(); //=> false
        p.tostring(); //=> “Anna,21”

    }
}

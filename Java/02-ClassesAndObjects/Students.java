public class Students {
    String studentId;
    Boolean studentIdValid;
    char semesterNumber;
    float avgGrade;
    String name;
    int age;

    public void studentInformation(){
        System.out.println("Student id: "+ studentId + ", is the id valid: " + studentIdValid + ", Semester: "+ semesterNumber + ", avgGrade: " +avgGrade);
    }
    public void sayHello(){
        System.out.println("Hello "+ name);
    }

    public void displayName(){
        System.out.println(name);
    }

    public void displayAge(){
        System.out.println(age);
    }

    public static void main(String[] args){
        Students myObj = new Students();
        myObj.studentId = "051734";
        myObj.name = "Billy";
        myObj.age = 17;
        myObj.studentIdValid = true;
        myObj.semesterNumber = '1';
        myObj.avgGrade = 3.78f;

        Students myObj2 =  new Students();
        myObj2.studentId = "123566";
        myObj2.name = "Kat";
        myObj2.age = 18;
        myObj2.studentIdValid = true;
        myObj2.semesterNumber = '3';
        myObj2.avgGrade = 4.28f;

        Students myObj3 = new Students();
        myObj3.studentId = "";
        myObj3.name = "Bob";
        myObj3.age = 15;
        myObj3.studentIdValid = false;
        myObj3.semesterNumber = '0';
        myObj3.avgGrade = 0f;


        //myObj.sayHello();
        myObj.displayName();
        myObj.displayAge();
        myObj.studentInformation();

        //myObj2.sayHello();
        myObj2.displayName();
        myObj2.displayAge();
        myObj2.studentInformation();

        //myObj3.sayHello();
        myObj3.displayName();
        myObj3.displayAge();
        myObj3.studentInformation();
    }
}

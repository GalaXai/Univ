import java.util.Arrays;
import java.util.OptionalDouble;

public class StudentGrades {
    String studentName;
    double[] grades;

     StudentGrades (String name, double[] grades) {
        this.studentName = name;
        this.grades = grades;
    }

    public OptionalDouble lowestGrade(){
         return Arrays.stream(grades).min();
    }

    public OptionalDouble highestGrade(){
         return Arrays.stream(grades).max();
    }

    public int numberOfGrades(){
         return grades.length;
    }

    public OptionalDouble avgOfGrades(){
        return Arrays.stream(grades).average();
    }

    public void studentRecord(){
         System.out.print(studentName + "Grades : ");
         for (Double i : grades){
             System.out.print(i + ", ");
         }
         System.out.println();
         System.out.println("lowest " + lowestGrade() + "highest grade " + highestGrade() + "avg of grades " + avgOfGrades() + "number of grades " +numberOfGrades());
    }

    public static void main(String[] args){
        StudentGrades Amanda = new StudentGrades("Amanda", new double[]{3.5, 4.5, 4.0, 2.0, 5.0, 3.5, 3.5});
        StudentGrades James = new StudentGrades("James", new double[]{2.0, 3.0, 2.0, 4.5, 4.5});

        Amanda.studentRecord();
        James.studentRecord(); //TODO learn about private values
    }


}

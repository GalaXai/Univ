public class Date {
    public static void main(String[] args) {
        String day = "Tuesday";
        int date_day = 4;
        int date_month = 10;
        int date_year = 2022;
        System.out.println(day+ " " + date_day + "."  + date_month + "." + date_year);
        // Display the value of each variable on a line by itself
        System.out.println(day);
        System.out.println(date_day);
        System.out.println(date_month);
        System.out.println(date_year);
        // Modify the program so that it displays the date in standard American format and standard European format
        System.out.println("American format: "+ day + ", " + date_month +" "+ date_day +", "+ date_year);
        System.out.println("European format: "+ day +" "+ date_day +"."+ date_month +"."+ date_year);
    }
}

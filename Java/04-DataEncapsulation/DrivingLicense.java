import java.text.MessageFormat;

public class DrivingLicense {
    private String name;
    private String surname;
    private String address;
    private String postalCode;
    private String city;
    private String id;
    private int yearOfIssue;
    private String category;

    public DrivingLicense(String name,String surname,String address,String postalCode,String city,String id,int yearOfIssue,String category){
        setName(name);
        setSurname(surname);
        setAddress(address);
        setPostalCode(postalCode);
        setCity(city);
        setID(id);
        setYearOfIssue(yearOfIssue);
        setCategory(category);
    }

    public void displayLicense(){
        System.out.println(MessageFormat.format("{0} {1} Category: {2}",getName(),getSurname(), getCategory()));
        System.out.println(MessageFormat.format("{0} {1} {2}",getPostalCode(),getCity(),getAddress()));
        System.out.println(MessageFormat.format("{0} {1}",getID(),getYearOfIssue()));
    }

    /// Getters
    public String getName(){return name;}
    public String getSurname(){return surname;}
    public String getAddress(){return address;}
    public String getPostalCode(){return postalCode;}
    public String getCity(){return city;}
    public String getID(){return id;}
    public int getYearOfIssue(){return yearOfIssue;}
    public String getCategory(){return category;}

    /// Setters
    public void setName(String name){
        name = name.toLowerCase();
        name = name.replace(name.charAt(0),Character.toUpperCase(name.charAt(0)));
        this.name = name;
    }
    public void setSurname(String surname){this.surname = surname;}
    public void setAddress(String address){this.address = address;}
    public void setPostalCode(String postalCode){this.postalCode = postalCode;}
    public void setCity(String city){this.city = city;}
    public void setID(String id){this.id = id;}
    public void setYearOfIssue(int yearOfIssue){
        if (yearOfIssue <= 2022  && yearOfIssue >= 1980){
            this.yearOfIssue = yearOfIssue;
        }
    }
    public void setCategory(String category){this.category = category;}

    public static void main(String[] args){
        DrivingLicense myObj = new DrivingLicense("Addison","Lewis","669 Main Street","21-431","Cracow","222326167",2021,"C");
        myObj.displayLicense();
    }

}
// {
//        "ID": "222326167"        "Name": "Addison Lewis"        "Address": "669 Main Street, Krakow, malopolskie, Poland 12-123"
//        "DOB": "12/2/1957"        "Class": "C"        "Sex": "F"        "YOI": "18/7/2021"        "EXP": "18/7/2026"    },

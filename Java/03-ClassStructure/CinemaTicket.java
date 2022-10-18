public class CinemaTicket {
    static String cinemaName;
    String filmTitle;
    int seatRow;
    int seatNumber;
    int price;
    public CinemaTicket(String Name, String Title, int row, int seat){
        cinemaName = Name;
        filmTitle = Title;
        seatRow = row;
        seatNumber = seat;
        if (row <= 2){
            price = 10;
        }else{
            price = 25;
        }
    }

    public void ticketData(){
        System.out.println(cinemaName + " Ticket for a " +filmTitle + "seat: "+ seatNumber + " row: " + seatRow + " price: " + price);
    }
    public static void main(String[] args){
        CinemaTicket myObj =  new CinemaTicket("Morning Star Cinema","Gladiator",2,13);
        CinemaTicket myObj2 =  new CinemaTicket("Morning Star Cinema","Gladiator",7,15);

        myObj.ticketData();
        myObj2.ticketData();

    }
}

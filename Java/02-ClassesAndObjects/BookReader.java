public class BookReader {
    String title;
    int realise_Year;
    String author;

    public void About(){
        System.out.println(title + "is a book written by " + author + " in " + realise_Year);
    }
    public static void main(String[] args){
        BookReader myObj = new BookReader();
        myObj.author = "Billy";
        myObj.title = "b0k";
        myObj.realise_Year = 2012;
        myObj.About();

    }
}

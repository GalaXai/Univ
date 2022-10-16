public class Rectangles {
    int hight;
    int width;

    public void display(){
        //****
        //*  *
        //****
        int hole = width - 2;
        // Printing the top
        for (int z = 0; z < width;z++){
            System.out.print('*');
        }
        // Printing the sides
        System.out.println();
        for (int i =0; i < hight-2; i++){
            System.out.print('*');
            for (int j = 0; j < hole;j++) {
                System.out.print(' ');
            }
            System.out.println('*');
        }
        // Printing the Bottom
        for (int z = 0; z < width;z++){
            System.out.print('*');
        }
        System.out.println();
    }

    public static void main(String[] args){
        Rectangles myObj =  new Rectangles();
        myObj.hight = 3;
        myObj.width = 7;
        myObj.display();

        myObj.hight = 2;
        myObj.width = 7;
        myObj.display();
    }
}

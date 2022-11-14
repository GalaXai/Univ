public class MyArray {

    public int even(int[] array){
        int counter = 0;
        for (int i =0; i <array.length; i++){
            if (array[i] %2 == 0){
                counter++;
            }
        }
        return counter;
    }
    public int positiveOdd(int[] array){
        int counter = 0;
        for (int i =0; i <array.length; i++){
            if (array[i] %2 != 0 && array[i] > 0){
                counter++;
            }
        }
        return counter;
    }
    public static void main(String[] args){
        MyArray MyArray = new MyArray();
        MyArray.even(new int[] {2,-6,5,8});
        MyArray.positiveOdd(new int []{3,2,-5,4,1,-7});

    }
}

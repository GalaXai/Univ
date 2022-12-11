import java.lang.reflect.Array;

public class Arrays2 {


    public static boolean arr(int[] arr, int[] arr2) {
        int count = 0;
        int count2 = 0;
        int x;
        for (int i = 0; i < arr.length; i++) {
            x = arr[i];
            if (x >= 10 && x <= 99) {
                count++;
            }
        }
        for (int j = 0; j < arr2.length; j++) {
            x = arr2[j];
            if (x >= 10 && x <= 99) {
                count2++;
            }
        }
        if (count == count2){
            return true;
        }else{return false;}
    }
    public static void main(String[] args){
        //Arrays2 a = new Arrays2();
        int[] arr1 = {15,8,2,37,49,117};
        int[] arr2 = {9,6,7,12,48,4,6,90,5};
        System.out.println(arr(arr1,arr2));
    }
}

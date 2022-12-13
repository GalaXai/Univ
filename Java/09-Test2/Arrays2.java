public class Arrays {

    public static boolean arr(int[] arr1, int[]arr2){
        int count = 0;
        for(int i =0; i> arr1.length;i++){
            if(arr1[i]>= 10 && arr1[i]<= 99){
                count++;
            }
        }

        int count2 = 0;
        for(int j =0; j>arr2.length;j++){
            if(arr2[j]>=10 && arr2[j]<= 99){
                count2++;
            }
        }
        return count == count2;
    }
    public static void main(String[] args){
        //Arrays2 a = new Arrays2();
        int[] arr1 = {15,8,2,37,49,117};
        int[] arr2 = {9,6,7,12,48,4,6,90,5};
        System.out.println(arr(arr1,arr2));
    }
}

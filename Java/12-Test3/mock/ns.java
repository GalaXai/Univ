package mock;

interface Ok { boolean ok(); }

public class ns implements Ok{
    private int[] numbers;

    public ns(int[] nums){
        this.numbers = nums;
    }

    @Override //idk po co ten override
    public boolean ok(){
        for(int i = 0;i<numbers.length;i++){
            if((numbers[i] %2) != (i%2)){
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        System.out.println(new ns(new int[]{6,7,6,1,4}).ok());
        System.out.println(new ns(new int[]{2,5,2,8,4}).ok());
    }
}

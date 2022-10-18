public class BasicStat {
    // Number of items within the specified range <x,y>
    public int itemsInRange(int x , int y){
        return y-x;
    }
    // Sum of numbers in the given range  <x,y>
    public int sumOfItemsInRange(int x, int y) {
        return (x-1 + y) * (y - x) / 2;
    }
    // Arithmetic mean of the numbers in the given range  <x,y>
    public int arithmeticMean(int x, int y) {
        return (x+y)/2;
    }
    public static void main(String[] args){
        BasicStat myObj = new BasicStat();
        System.out.println(myObj.arithmeticMean(5,10));
        System.out.println(myObj.itemsInRange(5,10));
        System.out.println(myObj.sumOfItemsInRange(5,10));
    }
}

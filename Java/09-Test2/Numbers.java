class Numbers {
    private int num1, num2, num3, num4, num5;

    // Constructor that accepts five int parameters
    public Numbers(int n1, int n2, int n3, int n4, int n5) {
        this.num1 = n1;
        this.num2 = n2;
        this.num3 = n3;
        this.num4 = n4;
        this.num5 = n5;
    }
    public boolean different() {
        // Check if all numbers are different
        return num1 != num2 && num1 != num3 && num1 != num4 && num1 != num5 && num2 != num3 && num2 != num4 && num2 != num5 && num3 != num4 && num3 != num5 && num4 != num5;
    }

    public static void main(String[] args){
        Numbers n = new Numbers(3, 4 ,2,1,6);
        System.out.println(n.different());
    }
}

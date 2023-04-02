public class C {

    public int[] nums;

    public C(int[] nums) {
        this.nums = nums;
    }

    public boolean m() {
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < nums[i - 1]) {
                return false;
            }
        }
        return true;
    }
}

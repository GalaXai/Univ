package mock;

public class Logic {
    private boolean log[];
    Logic(boolean input[]){
        this.log = input;
    }

    public int opposite(){
        int count = 0;
        for(int i = 1;i<log.length-1;i++){
            if(log[i-1] != log[i] && log[i+1] != log[i]){
                count++;
            }
        }
        return count;
    }
    public static void main(String[] args){
        System.out.println(new Logic(new boolean[] {true,false,false}).opposite());
        System.out.println(new Logic(new boolean[] { true,false,true,false }).opposite());
        System.out.println(new Logic(new boolean[] { true,false,true,true,false,true,false,true,false }).opposite());

    }
}
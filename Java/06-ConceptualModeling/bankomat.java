public class bankomat {
    private int balance;

    public bankomat(int balance){
        setBalance(balance);
    }

    private void setBalance(int balance) {
        this.balance = balance;
    }
    private int getBalance(){
        return balance;
    }

    public int withdraw(int amount){
        if (getBalance() - amount >= 0){
            this.balance -= amount;
            return amount;
        }else if (amount >= 500){
            System.out.println("The maximum withdraw amount is 500");
            return 0;
        }else{
            System.out.println("U dont have enough founds");
            return 0;
        }
    }
    public void deposit(int amount){
        this.balance += amount;
    }

    public void displayBalance(){
        System.out.println(getBalance());
    }

    public static void main(String[] args){
        bankomat p = new bankomat(0);
        p.deposit(500);
        p.displayBalance();
        p.withdraw(300);
        p.displayBalance();
        p.withdraw(300);
        p.withdraw(600);
    }
}
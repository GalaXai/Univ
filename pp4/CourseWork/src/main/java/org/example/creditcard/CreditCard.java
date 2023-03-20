package org.example.creditcard;

import java.math.BigDecimal;

public class CreditCard {
    private BigDecimal balance = BigDecimal.ZERO;
    private BigDecimal creditLimit = BigDecimal.ZERO;

    public CreditCard(String cardNumber){}

    public void assignCreditLimit(BigDecimal creditAmount){
        if(checkAssignLimit(creditAmount) && this.creditLimit.compareTo(BigDecimal.ZERO) < 0){
            throw new CreditBelowLimitException();
        }
        increaseBalance(creditAmount);
        this.creditLimit = creditAmount;
    }

    public void withdraw(BigDecimal withdrawAmmount){
        if(this.balance.compareTo(withdrawAmmount) >= 0 && this.creditLimit.compareTo(withdrawAmmount) >= 0){
            reduceBalance(withdrawAmmount);
            System.out.println("withdraw complited");
        }else{
            System.out.println("not enough credit");
        }

    }
    private static boolean checkAssignLimit(BigDecimal creditAmount) {
        // Returns -1 if smaller 0 if equal 1 if higher
        return creditAmount.compareTo(BigDecimal.valueOf(100)) <= 0;
    }

    public BigDecimal getBalance(){
        return balance;
    }

    private void increaseBalance(BigDecimal am) {this.balance = this.balance.add(am);}
    private void reduceBalance(BigDecimal am) {this.balance.subtract(am);}
}


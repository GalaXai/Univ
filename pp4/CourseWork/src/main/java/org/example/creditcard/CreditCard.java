package org.example.creditcard;

import java.math.BigDecimal;

public class CreditCard {
    private BigDecimal balance = BigDecimal.ZERO;
    private BigDecimal creditLimit = BigDecimal.ZERO; // Limited transaction to this Amount + When assigning adds Credit
    private BigDecimal debtAmount = BigDecimal.ZERO;
    private boolean isOnCredit = false;
    private int billingCount = 0;

    public CreditCard(String cardNumber){}

    public void assignCreditLimit(BigDecimal creditAmount){
        if(checkAssignLimit(creditAmount) && !isOnCredit){
            throw new CreditBelowLimitException();
        }
        this.isOnCredit = false;
        increaseBalance(creditAmount);
        this.creditLimit = creditAmount;
        this.debtAmount = creditAmount;
    }

    public void withdraw(BigDecimal withdrawAmount){
        if(this.balance.compareTo(withdrawAmount) >= 0 && this.creditLimit.compareTo(withdrawAmount) >= 0 && billingCount != 10){
            billingCount ++;
            reduceBalance(withdrawAmount);

            System.out.println("withdraw completed");
        }else{
            System.out.println("not enough credit");
        }

    }

    public void rePay(BigDecimal amount){
        // We don't want to overpay credit| If this is negative
         if(this.debtAmount.compareTo(amount) <=0){
             increaseBalance(amount.subtract(this.debtAmount));
             this.debtAmount = BigDecimal.valueOf(0);
             this.billingCount = 0;
             this.isOnCredit = false;

        }else{ // if amount is smaller
             this.debtAmount = this.debtAmount.subtract(amount);
             if(amount.compareTo(BigDecimal.valueOf(0)) != 0){
                 this.billingCount = 0;
             }
         }
    }

    public void payIn(BigDecimal amount){increaseBalance(amount);}
    private static boolean checkAssignLimit(BigDecimal creditAmount) {
        // Returns -1 if smaller, 0 if equal, 1 if higher
        return creditAmount.compareTo(BigDecimal.valueOf(100)) <= 0;
    }

    public BigDecimal getBalance(){
        return balance;
    }

    private void increaseBalance(BigDecimal am) {this.balance = this.balance.add(am);}
    private void reduceBalance(BigDecimal am) {this.balance = this.balance.subtract(am);}
}


package org.example.creditcard;

import java.math.BigDecimal;

public class CreditCard {
    private BigDecimal balance;

    public CreditCard(String cardNumber){}

    public void assignCreditLimit(BigDecimal creditAmount){
        // Returns -1 if smaller 0 if equal 1 if higher
        if(checkAssignLimit(creditAmount) && getBalance() == null){
            throw new CreditBelowLimitException();
        }
        this.balance = creditAmount;
    }


    private static boolean checkAssignLimit(BigDecimal creditAmount) {
        return creditAmount.compareTo(BigDecimal.valueOf(100)) <= 0;
    }

    public BigDecimal getBalance(){
        return balance;
    }
}

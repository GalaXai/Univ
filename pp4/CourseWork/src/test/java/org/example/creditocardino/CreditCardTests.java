package org.example.creditocardino;

import org.example.creditcard.CreditBelowLimitException;
import org.example.creditcard.CreditCard;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions. *;
import java.math.BigDecimal;
public class CreditCardTests {

    @Test
    void itAllowsToAssignCreditLimit(){

        CreditCard card = new CreditCard("1234-1234");

        card.assignCreditLimit(BigDecimal.valueOf(1000));

        assertEquals(BigDecimal.valueOf(1000),card.getBalance());

    }

    @Test
    void itAllowsToAssignDifferentCreditLimit() {
        //Arrange
        CreditCard card1 = new CreditCard("1234-5678");
        CreditCard card2 = new CreditCard("1234-5679");
        //Act
        card1.assignCreditLimit(BigDecimal.valueOf(1000));
        card2.assignCreditLimit(BigDecimal.valueOf(1100));
        //Assert // Then
        assertEquals(BigDecimal.valueOf(1000), card1.getBalance());
        assertEquals(BigDecimal.valueOf(1100), card2.getBalance());
    }

    @Test
    void itCantAssignLimitBelowCertainThreshold() {
        CreditCard card = new CreditCard("1234-1234");

        try{
            card.assignCreditLimit(BigDecimal.valueOf(10));
            fail("Should throw exception");
        } catch (CreditBelowLimitException e){
            assertTrue(true);
        }

        // We'll be using this type of testing.  I think.
        assertThrows(CreditBelowLimitException.class,
                () -> card.assignCreditLimit(BigDecimal.valueOf(99)));

        assertThrows(CreditBelowLimitException.class,
                () -> card.assignCreditLimit(BigDecimal.valueOf(100)));
    }
    @Test
    void itCantWithdrawMore(){
        CreditCard card = new CreditCard("1");

        card.assignCreditLimit(BigDecimal.valueOf(150));
        card.withdraw(BigDecimal.valueOf(200));
    }

    @Test
    void itCantWithdrawFromNone(){
        CreditCard card = new CreditCard("1");
        card.withdraw(BigDecimal.valueOf(200));
    }

    @Test
    void test(){
        BigDecimal a;
        BigDecimal b = BigDecimal.valueOf(100);
        System.out.println(a.compareTo(b));
    }
}

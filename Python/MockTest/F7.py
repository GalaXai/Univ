def bonus(n):
    wynik = 0
    for i in range(5):
        if n == 0:
            return wynik
        n -=1
        wynik +=100
    for j in range(3):
        if n == 0:
            return wynik
        n-=1
        wynik+=200
    while n != 0:
        n -=1 
        wynik +=50
    return wynik

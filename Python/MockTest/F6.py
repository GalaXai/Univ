def rand(begin,to):
    import random
    wynik = 1
    while (wynik % 2*3) != 0:
        wynik = random.randrange(begin,to)
    return wynik
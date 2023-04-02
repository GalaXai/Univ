"""Klasa, w ktorej mozna zrealizowac rozwiazanie Zadania 1"""

import uklad, wykresy
import iteracjaprosta, iteracjaseidela
import numpy as np

class Zadanie1:

    def __init__(self,wymiar=100):
        """Konstruktor"""
        self.n = wymiar
        self.k = 200 # liczba pomiarow dla jednej wartosci parametru
        self.norma = 1
    def testy(self):
        """Testy wstepne"""
        # miejsce na rozwiazanie pierwszej czesci zadania 1
        
        return 0
        
    def badaj_zbieznosc(self):
        #"""Zbieznosc/rozbieznosc metod iteracyjnych dla roznych macierzy"""
        u1 = uklad.Uklad(wymiar = self.n)
        u2 = uklad.Uklad(wymiar = 1000)


        #
        u1.losuj_uklad_symetryczny_dodatnio_okreslony()
        u2.losuj_uklad_symetryczny_dodatnio_okreslony()


        # rozwiazuje uklad z wykorzystaniem metody iteracji Seidela
        test1 = iteracjaseidela.IteracjaSeidela(ukl = u1)
        test2 = iteracjaseidela.IteracjaSeidela(ukl = u2)
        # wyznaczam macierz D i wektor C
        test1.przygotuj()
        test2.przygotuj()
        # iteracja Seidela
        test1.iteruj(
            iteracje = self.k,
            norma = self.norma)
        test2.iteruj(
            iteracje = self.k,
            norma = self.norma)
        seria1 = test1.normy.copy()
        seria2 = test2.normy.copy()
        niedokl1 = test1.sprawdz_rozwiazanie(self.norma)
        print(f"Niedokladnosc rozwiazania - iteracja Seidela: {niedokl1}")
        niedokl2 = test2.sprawdz_rozwiazanie(self.norma)
        print(f"Niedokladnosc rozwiazania - iteracja Seidela: {niedokl2}")
        # rysuje obie serie na wykresie
        wykres_test = wykresy.Wykresy()
        wykres_test.badaj_zbieznosc(
            tytul = "Zbieznosc metod iteracyjnych",
            opis_OY = "Normy przyblizen",
            dane1=seria1,
            opis1="Iteracja Seidela mniejsza",
            dane2 = seria2,
            opis2 = "Iteracja Seidela wieksza"
        )
        return 0
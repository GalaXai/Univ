SELECT SUM(liczba_godzin*stawka) FROM stopnie_tytuly
JOIN wykladowcy ON wykladowcy.stopien_tytul = stopnie_tytuly.stopien_tytul
JOIN wyklady ON wyklady.id_wykladowcy = wykladowcy.id_wykladowcy
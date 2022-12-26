SELECT * FROM wyklady
WHERE nazwa_wykladu like 'in%'

SELECT COUNT(nazwa_wykladu) AS liczba_wykladow,SUM(liczba_godzin) AS liczba_godzin FROM wyklady
WHERE nazwa_wykladu like 'in%'
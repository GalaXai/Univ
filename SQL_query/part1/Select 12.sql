SELECT * FROM wykladowcy
JOIN wyklady ON wyklady.id_wykladowcy = wykladowcy.id_wykladowcy
WHERE stopien_tytul = 'doktor'

SELECT * FROM wykladowcy
LEFT JOIN wyklady ON wyklady.id_wykladowcy = wykladowcy.id_wykladowcy
WHERE stopien_tytul = 'doktor' and id_wykladu is NULL
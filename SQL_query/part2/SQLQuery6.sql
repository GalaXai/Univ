SELECT wykladowcy.id_wykladowcy,nazwisko,imie FROM wykladowcy
LEFT JOIN wyklady ON wyklady.id_wykladowcy = wykladowcy.id_wykladowcy
JOIN pracownicy ON pracownicy.id_pracownika =  wykladowcy.id_wykladowcy
WHERE nazwa_wykladu is NULL
ORDER BY id_wykladowcy DESC
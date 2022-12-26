SELECT nazwa_wykladu,liczba_godzin,id_wykladu,id_wykladowcy,nazwisko,imie FROM wyklady
JOIN pracownicy ON wyklady.id_wykladowcy = pracownicy.id_pracownika
ORDER BY nazwa_wykladu,nazwisko,imie ASC

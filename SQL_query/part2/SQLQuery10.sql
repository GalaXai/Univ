SELECT nazwa_wykladu,liczba_godzin,nazwisko,imie,katedra FROM wyklady
JOIN wykladowcy ON wyklady.id_wykladowcy = wykladowcy.id_wykladowcy
JOIN pracownicy ON pracownicy.id_pracownika = wyklady.id_wykladowcy
WHERE nazwa_wykladu like 'Historia%'
ORDER BY nazwisko DESC
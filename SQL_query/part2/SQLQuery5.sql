SELECT nazwisko,imie,katedra FROM pracownicy
LEFT JOIN wykladowcy ON wykladowcy.id_wykladowcy = pracownicy.id_pracownika
ORDER BY nazwisko ASC, imie DESC
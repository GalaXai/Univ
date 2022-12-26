SELECT nazwisko,imie,stopien_tytul FROM wykladowcy
JOIN pracownicy ON wykladowcy.id_wykladowcy = pracownicy.id_pracownika
WHERE katedra = 'Katedra Informatyki'
ORDER BY nazwisko,imie ASC
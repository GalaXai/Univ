SELECT id_pracownika,nazwisko,imie FROM pracownicy
LEFT JOIN wykladowcy ON wykladowcy.id_wykladowcy = id_pracownika
WHERE katedra is NULL
ORDER BY nazwisko DESC,imie ASC
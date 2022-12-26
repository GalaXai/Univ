SELECT * FROM pracownicy
WHERE PESEL is NULL or data_zatrudnienia is NULL
ORDER BY nazwisko,imie ASC
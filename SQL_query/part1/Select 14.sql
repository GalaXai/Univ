SELECT COUNT(*) as brak_danych FROM pracownicy
WHERE data_zatrudnienia IS NULL and PESEL is NULL
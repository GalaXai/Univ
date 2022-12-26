SELECT DISTINCT nazwisko,imie,oceny_studentow.id_studenta,data_egzaminu FROM oceny_studentow
JOIN studenci ON oceny_studentow.id_studenta = studenci.id_studenta
ORDER BY data_egzaminu ASC
SELECT DISTINCT id_studenta
FROM oceny_studentow
WHERE data_egzaminu between '20170301' and '20170331'
ORDER BY id_studenta DESC
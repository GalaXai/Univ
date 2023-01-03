SELECT id_studenta FROM oceny_studentow
WHERE data_egzaminu = '20170412' AND id_studenta IN(
SELECT id_studenta FROM oceny_studentow
WHERE data_egzaminu =  '20171011')
ORDER BY id_studenta DESC
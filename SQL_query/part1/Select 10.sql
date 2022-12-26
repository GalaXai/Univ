SELECT * FROM studenci_wyklady
LEFT JOIN oceny_studentow ON oceny_studentow.id_studenta = studenci_wyklady.id_studenta and oceny_studentow.id_wykladu = studenci_wyklady.id_wykladu 
WHERE ocena is NULL	

-- another way

SELECT id_studenta,id_wykladu
FROM studenci_wyklady

EXCEPT
	
SELECT id_studenta,id_wykladu FROM oceny_studentow
SELECT studenci.id_studenta,nazwisko,imie FROM studenci
JOIN studenci_wyklady ON studenci_wyklady.id_studenta =  studenci.id_studenta
WHERE id_wykladu = 4  AND studenci.id_studenta IN (SELECT id_studenta FROM studenci_wyklady WHERE id_wykladu = 11)


SELECT imie, nazwisko, id_studenta
FROM studenci
WHERE id_studenta IN			
	(SELECT id_studenta
	 FROM studenci_wyklady
	 WHERE id_wykladu=11 AND id_studenta IN
(SELECT id_studenta
FROM studenci_wyklady
WHERE id_wykladu=4))

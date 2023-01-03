SELECT studenci.id_studenta,nazwisko FROM studenci
LEFT JOIN oceny_studentow ON studenci.id_studenta=oceny_studentow.id_studenta
WHERE ocena is NULL
ORDER BY studenci.id_studenta,nazwisko ASC
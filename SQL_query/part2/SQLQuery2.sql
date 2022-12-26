SELECT nazwisko,imie FROM studenci_wyklady
JOIN studenci ON studenci_wyklady.id_studenta=studenci.id_studenta
JOIN wyklady ON studenci_wyklady.id_wykladu = wyklady.id_wykladu
WHERE nazwa_wykladu = 'Statystyka'
ORDER BY nazwisko,imie ASC
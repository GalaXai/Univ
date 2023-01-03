SELECT pracownicy.nazwisko,pracownicy.imie,pracownicy.PESEL	AS pesel_grupa,nazwa_wykladu FROM pracownicy
JOIN wyklady on pracownicy.id_pracownika = wyklady.id_wykladowcy
UNION
SELECT nazwisko, imie, nr_grupy AS pesel_grupa, nazwa_wykladu FROM studenci
LEFT JOIN studenci_wyklady ON studenci_wyklady.id_studenta= studenci.id_studenta
LEFT JOIN wyklady ON studenci_wyklady.id_wykladu = wyklady.id_wykladu
ORDER BY pesel_grupa, nazwisko, imie

SELECT studenci.nazwisko,studenci.imie,nazwa_wykladu,pracownicy.nazwisko AS NazwiskoWykladowcy,katedra
FROM studenci
LEFT JOIN studenci_wyklady ON studenci.id_studenta =  studenci_wyklady.id_studenta
LEFT JOIN wyklady ON wyklady.id_wykladu=studenci_wyklady.id_wykladu
LEFT JOIN pracownicy ON wyklady.id_wykladowcy = pracownicy.id_pracownika
LEFT JOIN wykladowcy ON wyklady.id_wykladowcy = wykladowcy.id_wykladowcy

ORDER BY nazwa_wykladu DESC, pracownicy.nazwisko ASC
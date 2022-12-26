SELECT id_studenta AS student_wykladowca,studenci.nr_grupy AS grupa_katedra
FROM studenci
JOIN grupy ON studenci.nr_grupy = grupy.nr_grupy
WHERE grupy.nr_grupy LIKE 'DMIe%'

UNION

SELECT id_wykladowcy AS student_wykladowca, katedra AS grupa_katedra
FROM wykladowcy
ORDER BY grupa_katedra ASC
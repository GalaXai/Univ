SELECT DISTINCT * FROM wyklady
JOIN studenci_wyklady ON studenci_wyklady.id_wykladu = wyklady.id_wykladu
LEFT JOIN oceny_studentow ON oceny_studentow.id_wykladu = wyklady.id_wykladu
WHERE ocena is NULL
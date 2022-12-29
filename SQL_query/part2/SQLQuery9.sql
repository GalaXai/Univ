SELECT wyklady.id_wykladu,nazwa_wykladu FROM wyklady
LEFT JOIN studenci_wyklady ON studenci_wyklady.id_wykladu=wyklady.id_wykladu
WHERE id_studenta is NULL
ORDER BY nazwa_wykladu DESC
def month(n):
    Miesiace = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec",
            "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
    return Miesiace[n-1]
for x in range(1,13):
    print(month(x))
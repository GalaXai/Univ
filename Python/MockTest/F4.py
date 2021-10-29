def coins(price):
    reszta = (price % 5)
    x = (price // 5)
    n_reszta = (reszta % 2)
    y = reszta // 2
    z = (n_reszta // 1)
    return x+y+z
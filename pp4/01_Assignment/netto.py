def calc_netto(brutto_ammount,tax):
    if tax >=0:
        return round(brutto_ammount/(1+(tax/100)),2)
    else:
        raise Exception("Tax value should be positive number")

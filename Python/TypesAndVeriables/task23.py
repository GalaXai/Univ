ammount = float(input("Type in the price: "))
price_wVat = ammount / 1.23
costOfTheVat = ammount - price_wVat
print("Ammount {}".format(ammount))
print("VAT 23% {:.2f}".format(costOfTheVat))
print("Ammount wichout vat {:.2f}".format(price_wVat))

y = True
pocet = 0
sucet = 0
while y:
    x = input("Zadaj číslo: ")
    if (x == "koniec"):
        priemer = sucet/pocet
        print("Priemer je ",priemer)
        y = False
    else:
        sucet = sucet + int(x)
        pocet = pocet + 1
        

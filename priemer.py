y = True
p = 0
s = 0
while y:
    x = input("Zadaj číslo: ")
    if (x == "koniec"):
        print ("Priemer je ", s/p)
    else:
        s = s + int(x)
        p = p + 1
        y = False

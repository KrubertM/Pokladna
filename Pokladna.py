print("Vítejte v obchodě")
print("Elektronika, Potraviny, Oblečení")
print("Napíš odejít pokud budeš chtít ukončit nákup")

run = True
Zbozi = []
cena = 0

while run:
    kde = input("Zadej kam chceš: ")
    
    if(kde == "Elektronika"):
        print("Vítej v elektonice")
        elektronika = ["Počítač - 10000kč", "Telefon - 8000kč", "Kamera - 12000kč"]
        print("Vyber jsi věc Počítač, Telefon, Kamera: ")
        co = input("Zadej zboží: ")
        Zbozi.append (co)
        if (co == "Počítač"):
            cena = cena + 10000
        if (co =="Telefon"):
            cena = cena + 8000
        if( co =="Kamera"):
            cena = cena + 12000


    if(kde == "Potraviny"):
        print("Vítej v potravinách")
        potraviny = ["Chelba - 130kč", "Rohlík - 2kč", "Okurka - 50kč"]
        print("Vyber jsi věc Chleba, Rohlík, Okurka: ")
        co = input("Zadej zboží: ")
        Zbozi.append (co)
        if (co == "Chleba"):
            cena = cena + 130
        if (co =="Rohlík"):
            cena = cena + 2
        if( co =="Okurka"):
            cena = cena + 50


    if(kde =="Oblečení"):
        print("Vítej v oblečení")
        oblečení = ["Tričko - 1000", "Kalhoty - 800kč", "Ponožky - 100kč"]
        print("Vyber jsi věc Tričko, Kalhoty, Ponožky: ")
        co = input("Zadej zboží: ")
        Zbozi.append (co)
        if (co == "Tričko"):
            cena = cena + 1000
        if (co =="Kalhoty"):
            cena = cena + 800
        if( co =="Ponožky"):
            cena = cena + 100

    if(kde == "Odejít"):
        break

print("Vaše konečné zboží: ")
print(*Zbozi)
print("Vaše konečná cena: ")
print(cena)

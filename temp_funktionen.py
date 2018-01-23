#Temperaturen in Skalensysteme umwandeln mittels Funktionen


ABSOLUTER_NP_C = -273.15
NULL_F = 32.0
ABSOLUTER_NP_K = 0.0
ABSOLUTER_NP_F = -459.67
FAKTOR_F_C = 1.8 
FEHLERMELDUNG_TEMP = "Fehler: unmoegliche Temperatur!"

def get_float(msg = "Bitte Zahl eingegben: "):
    while True:
        try:
            f = float(input(msg))
            return f
        except ValueError:
            print("Ungueltige Eingabe! Bitte nochmal!")

def c_to_k(x):
    if x >= ABSOLUTER_NP_C:
        return x - ABSOLUTER_NP_C
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)

def c_to_f(x):
    if x >= ABSOLUTER_NP_C:
            return NULL_F + FAKTOR_F_C * x
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)
def k_to_c(x):
    if x >= ABSOLUTER_NP_K:
        return x + ABSOLUTER_NP_C
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)
def k_to_f(x):
    if x >= ABSOLUTER_NP_K:
        return x * 1.8 - 241.15
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)
def f_to_c(x):
    if x >= ABSOLUTER_NP_F:
        return (x - NULL_F) / 1.8
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)
def f_to_k(x):
    if x >= ABSOlUTER_NP_F:
        return (x - ABSOLUTER_NP_F) / 1.8
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)
wahl = -1
while wahl != 0:
    wahl = int(input("Bitte waehlen: "))


    if wahl == 1:
        x = get_float("Temperatur in Celsius eingeben: ")
        print (x, "Grad =",  c_to_k(x), "Kelvin")   
    elif wahl == 2:
        x = get_float("Temperatur in Celsius eingeben: ")
        print (x, "Grad =", c_to_f(x), "Fahrenheit")
    elif wahl == 3:
        x = get_float("Temperatur in Kevlin eingeben: ")
        print (x, "Kelvin = ", k_to_c(x), "Grad")
    elif wahl == 4:
        x = get_float("Temperatur in Kevlin eingeben: ")
        print (x, "Kelvin =", k_to_f(x), "Fahrenheit")
    elif wahl == 5:
        x = get_float("Temperatur in Fahrenheit eingeben: ")
        print(x, "Fahrenheit =", f_to_c(x), "Celsius")
    elif wahl == 6:
        x = get_float("Temperatur in Fahrenheit eingeben: ")
        print(x, "Fahrenheit =", f_to_k(x), "Kevlin")
    else:
        print("Programm wurde vom Nutzer beendet.")
        break


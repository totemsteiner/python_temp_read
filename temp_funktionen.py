#Temperaturen in Skalensysteme umwandeln mittels Funktionen


ABSOLUTER_NP_C = -273.15
NULL_F = 32.0
ABSOLUTER_NP_K = 0.0
ABSOLUTER_NP_F = -459.67
FAKTOR_F_C = 9/5
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
        if x >= 

wahl = -1
wahl = int(input("Bitte waehlen: "))


if wahl == 1:
    x = get_float("Temperatur in Celsius eingeben: ")
    print (x, "Grad =",  c_to_k(x), "Kelvin")   
elif == 2:
    x = get_float("Temperatur in Celsius eingeben: ")
    print(x, "Grad = ", c
    


import sys
import logging
logging.basicConfig(level=logging.DEBUG)

operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
a = float(input("podaj składnik 1. "))
b = float(input("podaj składnik 2. "))
if (operation == "1"):
    logging.info("Wykonanie operacji dodawania dla liczb : %s i %s", a, b )
    print("Wynik to: ",a + b)
if (operation == "2"):
    logging.info("Wykonanie operacji odejmowania dla liczb : %s i %s", a, b )
    print("Wynik to: ",a - b)
if (operation == "3"):
    logging.info("Wykonanie operacji mnożenia dla liczb : %s i %s", a, b )
    print("Wynik to: ",a * b)
if (operation == "4"):
    logging.info("Wykonanie operacji dzielenia dla liczb : %s i %s", a, b )
    print("Wynik to: ",a / b)    


#Math Functions
#sqrt() - atgriež skaitļa kvadrātsakni
import math

def piemers12():
    input_number = float(input("Ievadi skaitli, kura kvadrātsakni vēlies atrast: "))
    result = math.sqrt(input_number)
    print(result)
    return result
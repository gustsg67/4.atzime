import math
#Math Functions
#cbrt() - atgriež skaitļa kubsakni

def piemers14():
    input_number = float(input("Ievadi skaitli, kura kubsakni vēlies atrast: "))
    result = math.cbrt(input_number)
    print(result)
    return result
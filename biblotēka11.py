#Math Functions
#fact() - atgriež skaitļa faktoriāli
import math

def piemers11():
    input_number = int(input("Ievadi skaitli, kura faktoriālu vēlies atrast: "))
    result = math.factorial(input_number)
    print(result)
    return result
import math
#Math Functions
#pow() - returns the value of a number raised to the power of another number

def piemers13():
    base = float(input("Ievadi bāzi: "))
    exponent = float(input("Ievadi eksponentu: "))
    result = math.pow(base, exponent)
    print(result)
    return result
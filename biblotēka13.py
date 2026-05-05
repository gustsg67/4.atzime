import math
#Math Functions
#pow() - atgriež skaitļa vērtību, paceltu citas skaitļa pakāpē

def piemers13():
    print("Šeit varēsi izvēlēties bāzi un eksponentu, lai aprēķinātu bāzes pakāpi!")
    base = float(input("Ievadi bāzi: "))
    exponent = float(input("Ievadi eksponentu: "))
    result = math.pow(base, exponent)
    print(result)
    return result
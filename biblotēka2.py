import math
#Math Functions
#log10() - atgriež skaitļa desmitniekšķirnes logaritmu

def piemers2():
    input_number = float(input("Ievadi skaitli kura desmitniekšķirnes logaritmu vēlies uzzināt: "))
    result = math.log10(input_number)
    print(result)
    return result


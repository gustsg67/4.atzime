#Built-in Functions
#round() - noapaļo skaitli uz norādīto decimāldaļu skaitu

def piemers3():
    input_number = float(input("Ievadi skaitli kuru vēlies noapaļot: "))
    decimal_places = int(input("Ievadi līdz kādai decimāldaļai vēlies noapaļot iepriekš doto skaitli: "))
    result = round(input_number, decimal_places)
    print(result)
    return result
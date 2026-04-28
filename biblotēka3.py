#Built-in Functions
#round() - rounds a number to a specified number of decimal places

def piemers3():
    input_number = float(input("Ievadi skaitli: "))
    decimal_places = int(input("Ievadi decimāldaļu skaitu: "))
    result = round(input_number, decimal_places)
    print(result)
    return result
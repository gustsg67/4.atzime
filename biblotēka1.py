
#Built-in Functions
#bin() - pārvērš veselu skaitli binārajā virknes formā


def piemers1():
    input_number = int(input("Ievadi skaitli kuru pārvērtis binārajā formā: "))
    result = bin(input_number)
    print(result)
    return result
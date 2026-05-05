#Built-in Functions
#float() - pārvērš skaitli vai virkni par "floating" punkta skaitli

def piemers8():
    print("Šeit varēsi pārvērst skaitli vai tekstu par decimāldaļu!")
    input_value = input("Ievadi skaitli vai tekstu, ko vēlies pārvērst par decimāldaļu: ")
    result = float(input_value)
    print(result)
    return result

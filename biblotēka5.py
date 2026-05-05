#Built-in Functions
#complex() - pārvērš skaitli vai virkni par kompleksu skaitli

def piemers5():
    input_value = input("Ievadi skaitli vai tekstu, ko vēlies pārvērst par kompleksu skaitli: ")
    result = complex(input_value)
    print(result)
    return result
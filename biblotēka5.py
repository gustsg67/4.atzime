#Built-in Functions
#complex() - converts a number or a string to a complex number

def piemers5():
    input_value = input("Ievadi skaitli vai tekstu, ko vēlies pārvērst par kompleksu skaitli: ")
    result = complex(input_value)
    print(result)
    return result
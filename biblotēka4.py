#Built-in Functions
#sum() - returns the sum of all items in an iterable

def piemers4():
    input_numbers = input("Ievadi skaitļus, atdalot tos ar komatu: ")
    numbers_list = [float(num) for num in input_numbers.split(",")]
    result = sum(numbers_list)
    print(result)
    return result
#Built-in Functions
#sum() - atgriež visu elementu summu iterējamā objektā

def piemers4():
    input_numbers = input("Ievadi vizmaz 3 skaitļus, atdalot tos ar komatu: ")
    if len(input_numbers.split(",")) < 3:
        print("Lūdzu ievadi vizmaz 3 skaitļus!")
        return None
    else:
        numbers_list = [float(num) for num in input_numbers.split(",")]
        result = sum(numbers_list)
        print(result)
        return result
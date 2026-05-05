import random
#Random Functions
#rand.choice() - atgriež nejaušu elementu no neaizpildītas secības

def piemers10():
    print("Šeit varēsi izvēlēties elementus, no kuriem tiks nejauši izvēlēts viens!")
    input_sequence = input("Ievadi elementus, atdalot tos ar komatu: ")
    elements_list = [elem.strip() for elem in input_sequence.split(",")]
    result = random.choice(elements_list)
    print(result)
    return result
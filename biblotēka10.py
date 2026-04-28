import random
#Random Functions
#rand.choice() - returns a random element from a non-empty sequence

def piemers10():
    input_sequence = input("Ievadi elementus, atdalot tos ar komatu: ")
    elements_list = [elem.strip() for elem in input_sequence.split(",")]
    result = random.choice(elements_list)
    print(result)
    return result
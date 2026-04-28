import random
#Random Functions
#rand.uniform() - returns a random float number between a specified range

def piemers9():
    lower_bound = float(input("Ievadi apakšējo robežu: "))
    upper_bound = float(input("Ievadi augšējo robežu: "))
    result = random.uniform(lower_bound, upper_bound)
    print(result)
    return result
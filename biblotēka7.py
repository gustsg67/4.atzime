import random
#Random Functions
#randomint() - returns a random integer between a specified range

def piemers7():
    lower_bound = int(input("Ievadi apakšējo robežu: "))
    upper_bound = int(input("Ievadi augšējo robežu: "))
    result = random.randint(lower_bound, upper_bound)
    print(result)
    return result
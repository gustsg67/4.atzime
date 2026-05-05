import random
#Random Functions
#randomint() - atgriež nejaušu skaitli starp norādīto diapazonu un 1,0

def piemers7():
    print("Šeit varēsi izvēlēties diapazonu, no kura tiks ģenerēts nejaušs skaitlis!")
    lower_bound = int(input("Ievadi apakšējo robežu: "))
    upper_bound = int(input("Ievadi augšējo robežu: "))
    result = random.randint(lower_bound, upper_bound)
    print(result)
    return result
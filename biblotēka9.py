import random
#Random Functions
#rand.uniform() - atgriež nejaušu "floating" skaitli norādītajā diapazonā

def piemers9():
    print("Šeit varēsi izvēlēties diapazonu, no kura tiks ģenerēts nejaušs skaitlis!")
    lower_bound = float(input("Ievadi apakšējo robežu: "))
    upper_bound = float(input("Ievadi augšējo robežu: "))
    result = random.uniform(lower_bound, upper_bound)
    print(result)
    return result
from random import randint #per fare la scelta random, tipo lancio di moneta
import random
import string


def length(): #per la lunghezza della nuova variabile o funzione (per il nome inteso)
    """
    Returns a random integer used as length for the key name.
    """
    return randint(5,20)


def cap_letter(): #per le lettere in uppercase
    """
    Random generator for uppercase letter (M,O).
    """
    letters = string.ascii_uppercase
    random_letter = random.choice(letters)
    #Generate random letter
    
    #print(random_letter)
    return random_letter


def low_letter(): #per le lettere il lowercase
    """
    Random generator for lowercase letter
    """
    letters = string.ascii_lowercase
    random_letter = random.choice(letters)
    #Generate random letter
    
    #print(random_letter)
    return random_letter

def choice_letter(): #sceglie una lettera a casa 
    """
    Random generator for choosing the next letter.
    """
    if randint(0,1) == 0:
        return cap_letter()
    else:
        return low_letter()


def generate(): #genera un nuovo nome di variabile/funzione in modo random
    """
    Generates a new variable/function name.
    """
    key = ''
    for i in range(0, length()):
        key+=choice_letter()
    return key


lista = [] #list
a = generate()
lista.append(a)
count = 1
a = generate()
while a not in lista:
    lista.append(a)
    count+=1
    print(count)
    a = generate()

print("Ho trovato due casi uguali!")
print(a)
print("Dopo ", count, " tentativi.")
print(lista)
from random import randint #per fare la scelta random, tipo lancio di moneta


def length(): #per la lunghezza della nuova variabile o funzione (per il nome inteso)
    """
    Returns a random integer used as length for the key name.
    """
    return randint(5,20)


def cap_letter(): #per le lettere in uppercase
    """
    Random generator for uppercase letter (M,O).
    """
    if randint(0,1) == 0:
        return 'M'
    else:
        return 'O'


def low_letter(): #per le lettere il lowercase
    """
    Random generator for lowercase letter (m,o).
    """
    if randint(0,1) == 0:
        return 'm'
    else:
        return 'o'


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

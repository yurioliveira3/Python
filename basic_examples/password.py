# Escreva um programa que gere uma passwd aleatória que atenda condições:
# (1) deve ter 10 characters
# (2) deve conter duas letras maiúsculas
# (3) deve conter 1 dígito
# (4) deve conter um símbolo
import string
import random

if __name__ == "__main__":
    
    characters_general = string.ascii_letters
    characters_lower = string.ascii_lowercase
    characters_upper = string.ascii_uppercase
    symbol = string.punctuation
    digit = string.digits
    passwd = ''

    for i in range(0,10):
        if i < 1: #add a digit and symbol
            passwd += random.choice(digit)
            passwd += random.choice(symbol)
        if i < 2: #add 2 upper case characters
            passwd += random.choice(characters_upper)
        if i > 2: #add another 8 characters
            passwd += random.choice(characters_lower)

    #Randomize crated passwd
    passwd = ''.join(random.sample(passwd, len(passwd)))

    print(passwd)
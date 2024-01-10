import random as r

# r.seed(105) # to wartość, która inicjuje generator
'''
 random.seed(a=None, version=2)
    Initialize the random number generator.

    If a is omitted or None, the current system time is used. 
    If randomness sources are provided by the operating system, 
    they are used instead of the system time (see the os.urandom() function for details on availability).
''' 

print(r.random()) # liczba rzeczywista z zakresu <1, 0)
print(r.uniform(10, 100)) # liczba rzeczywista z zakresu <a, b)
print(r.randint(10,100)) # całkowita z <10, 100)

napis = "ekodekjkjkju" # napis jest sekwencją w Python
print(r.choice(napis)) # losuje element z podanej sekwencji

import numpy as np
import string
import random
size=input("Enter the size of password: ")
password = ""
rng = np.random.default_rng()
upper = rng.choice(list(string.ascii_uppercase))
# Get a random uppercase letter
password+=upper
lower = rng.choice(list(string.ascii_lowercase))
# Get a random lowercase letter
password+=lower
special_chars = string.punctuation
# Get all the special characters from the string module
random_special_char = random.choice(special_chars)
# Generate a single random special character
password+=random_special_char
random_number = rng.integers(low=0, high=10)
# Generate a random number between 0 and 10
password+=str(random_number)
while len(password)<int(size): #check if the length of password the user wants is less than the current length of the password
    password+=random.choice(special_chars)
    if len(password)<int(size): # to make more variety in the password
        password+=rng.choice(list(string.ascii_uppercase))
    if len(password)<int(size):
        password+=rng.choice(list(string.ascii_lowercase))
    if len(password)<int(size):
        password+=str(random_number)
print("Your password is: ",password)
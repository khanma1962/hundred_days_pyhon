#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# random.seed(42)
pass_wrd = []

for i in range(nr_letters):
    pass_wrd.append(random.choice(letters))
for i in range(nr_numbers ):
    pass_wrd.append(str(random.choice(numbers)))
for i in range(nr_symbols):
    pass_wrd.append(str(random.choice(symbols)))
    
print(pass_wrd)
print(len(pass_wrd))

random.shuffle(pass_wrd)


pass_wrd_new = ''
for ch in pass_wrd:
    pass_wrd_new += ch

print(f"Shuffled pass is {pass_wrd_new}")


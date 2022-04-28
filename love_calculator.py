'''
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

'''

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true_score, love_score, score = 0, 0, 0
name1, name2 = name1.lower(), name2.lower()
# temp = name1.count('m')
# print(temp)
for c1 in "TRUE".lower():
    name1_count = name1.count(c1)
    name2_count = name2.count(c1)
    true_score += name1_count
    true_score += name2_count
    # print(n1)
# print(f"true love is {true_score}")

for c2 in "LOVE".lower():
    name1_count = name1.count(c2)
    name2_count = name2.count(c2)
    love_score += name1_count
    love_score += name2_count
    # print(n1)
# print(f"love score is {love_score}")

score = int(str(true_score) + str(love_score))

#conditional statements
if(score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif(score >= 40 and score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")




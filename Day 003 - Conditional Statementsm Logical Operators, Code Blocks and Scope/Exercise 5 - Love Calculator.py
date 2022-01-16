# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine = (name1 + name2).lower()
true_score = combine.count('t')
true_score += combine.count('r')
true_score += combine.count('u')
true_score += combine.count('e')
love_score = combine.count('l')
love_score += combine.count('o')
love_score += combine.count('v')
love_score += combine.count('e')
score = int(str(true_score) + str(love_score))
if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

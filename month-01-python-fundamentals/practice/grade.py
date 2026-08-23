score = float(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("You got an A!")

elif score < 90 and score >=80:
    print("You got a B!")

elif score < 89 and score >=70:
    print("You got a C!")

elif score < 70 and score >= 60:
    print("You got a D!")

else:
    print("You got an F!")
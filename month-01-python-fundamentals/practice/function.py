def grades():
    grade = input("Enter your grade: ").strip().upper()

    if grade == "A":
        print("You got an A grade")
    elif grade == "B":
        print("You got a B grade")
    elif grade == "C":
        print("You got a C grade")
    elif grade == "D":
        print("You got a D grade")
    else:
        print("Invalid grade")


def main():
    while True:
        grades()
        again = input("Do you wish to continue? (Y/N): ")

        if again != "y" or again != "Y":
            break


main()
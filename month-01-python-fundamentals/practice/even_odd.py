def main():
    x = int(input("Enter a number: "))

    if is_even(x):
        print("The number is even.")

    else: 
        print("The number is odd.")

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

main()
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def main():
    x = int(input("Enter a number: "))

    if is_even(x):
        print("Even")

    else: 
        print("Odd")

main()
'''while True:
    number = int(input("What's n? = "))
    if number > 0:
      break

for index in range(number):
   print("Hello")'''


def main():
    n = int(input("Enter number = "))
    hello(n)

def hello(n):
    for index in range(n):
        print("Hello")
main()
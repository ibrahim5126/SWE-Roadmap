#ask user his/her name
name = input("Enter your name: ").strip().title() #Removes whitespace from beginning and end of string and capitalizes first letter of each word

first, last = name.split()

print(f"Hello {first} {last}!")

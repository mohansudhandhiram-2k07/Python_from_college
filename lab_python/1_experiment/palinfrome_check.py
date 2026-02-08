#to check the given number for palindrome

number = int(input("ENTER NUMBER TO CHECK PALINDROME: "))
to_check = number
answer = 0
while number != 0:
    temp = number % 10
    answer = answer * 10 + temp
    number //= 10

if answer == to_check:
    print(f"the entered number is palindrome!")
else:
    print(f"the entered number is not palindrome!")
#swaping of two numbers using XOR

a = eval(input("enter number to swap(1): "))
b = eval(input("enter number to swap(2): "))

print(f"NUMBER 1 BEFORE SWAPPING: {a}")
print(f"NUMBER 2 BEFORE SWAPPING: {b}\n")

# a = a^b
# b = a^b
# a = a^b
a,b = b,a


print(f"NUMBER 1 AFTER SWAPPING: {a}")
print(f"NUMBER 2 AFTER SWAPPING: {b}")

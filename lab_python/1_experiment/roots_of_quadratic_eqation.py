#finding roots of quadratic numbers

import cmath as cm

print(f"ax^2+bx+c")
a = int(input(f"enter value for a: "))
if a == 0:
    print("Not a quadratic equation (a cannot be 0)")
    exit()
b = int(input(f"enter value for b: "))
c = int(input(f"enter value for c: "))

ans2 = ((-b)+(cm.sqrt((b*b)-4*a*c)))/(2*a)
ans1 = ((-b)-(cm.sqrt((b*b)-4*a*c)))/(2*a)

print(f"root 1 is {ans1}")
print(f"root 2 is {ans2}")
number = int(input("ENTER N: "))
answer = 0
for i in range(number+1):
    if not i&1:
        answer += i
print(answer)

# a = 10
# b = 22.5
# c = 10 + 46j

# print("type of a is ",type(a),)
# print("type of b is ", type(b))
# print("type of c is ",type(c))
# print("The imaginary part of 'c' is ",c.imag,"\nThe real part of 'c' is ",c.real)

# binary = format(a,'x')
# print("Binary = ",binary)
# decimal = int(binary,16)
# print("Decimal = ",decimal)
# print(f"mohan{10}")
# students = ['naveen','mohan','kumaar']
# lang = ["c++","c","python"]
# print(f"{students}")
# print(f"{students[-2]}")                  #reverse index is possible
# print(f"{students[1:3]}")                 #list slicing
# print(f"{students + lang}")               #concatanate
# students.insert(9,"pavan")                #insert (there is no check for end index)
# print(f"{students}")

# # intro on tuple

# chocolate = ("manoj","palani","lithish")    #modification not possible
# print(f"{chocolate}")

# #chocolate.insert(1,"kavin")               #error
# print(f"{chocolate}")       
# #chocolate.delete(1,"kavin")               #error
# print(f"{students} + {chocolate}")        #error - can cat list & tuple


# # intro on frozen sets

# fruits = {"apple","banana","pineapple"}     #{} - set, [] - list, () - tuple
# print(f"{fruits}")
# freezed_set = frozenset(fruits)
# print(f"{type(freezed_set)}")               #frozen set 


# fruits.add("mango")                         #random insertion(add)
# print(f"{fruits}")


# # intro on dictionary

# student = {"name": "Mohan", "gpa": 9}
# print(f"{student['name']}")                 # 1. READ
# student['gpa'] = 10                         # 2. WRITE (Update value)

# student['college'] = "Sri Eshwar"           # 3. ADD (New key)
# print(f"{student}")


# # Range

# for i in range(1,11,2):                        #range(start,stop,step) 
#     print(f"{i}")

# # TEST IN CLASS 

# animals = ["lion","tiger","monkey"]
# bird = ["crow","hen","peacock"]
# cat_list = animals + bird
# print(f"{cat_list}")
# print(f"{cat_list[3]}")
# print(f"{cat_list[-3]}")

# tup_list = tuple(cat_list)
# print(f"{tup_list}")

# set_list = set(tup_list)
# print(f"{set_list}")

# set_list.add("naveen")
# print(f"{set_list}")

# frozen_set = frozenset(set_list)
# print(f"{frozen_set}")

# #frozen_set.add("not possible")                       #AttributeError: 'frozenset' object has no attribute 'add'

# name = input("enter your name: ")
# age = input(f"Hello {name},what is your age?\n")        #getting input from user. 
# print(f"Good to know that you are {age} years old!!")
# print(type(age))                                        #returns string ONLY!!
# age = int(age)
# print(type(age))                                        #typecasted to int


# # operators in python

# a = int(input("enter for 'a': "))
# b = int(input("enter for 'b': "))
# c = 15

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)
# print(a<b)
# print(a>b)
# print(a==b)
# print(a!=b)

# print(not a)        #return bool values
# print(a and b)      #second value is displayed 'b'
# print(a or b)       #first value is displayed 'a'

# print(a & b)
# print(a | b)
# print(a ^ b)

# print(a is b)
# print(a is not b)

# List = [10,20,30]
# print(a in List)

# #TERNARY OPERATOR

# min = a if a < b else b
# print(min)

# #conditional operator if,elif,else
# num = int(input("ENTER THE NUMBER TO COMPARE WITH '10': "))
# if(num>10):
#     print(f"{num} is larger than 10")
# elif(num == 10):
#     print(f"{num} is equal to 10")
# else:
#     print(f"{num} is smaller than 10")

# There are 33 key word in python

#  True,False,None - starting in capital
#  and,or,is
#  if,elif,else
#  while,for,break,continue,return,in,yield
#  try,except,finally,raise,assert
#  import,from,as,class,def,pass,global,nonlocal,lambda,del,with

# #while loop

# while True:
#     print("haha")

# for i in range(1,101):
#     print(i)
#     if(i == 5):
#         pass                  #pass is used as a place holder

# #function

# # without arg and return type
# def add():
#     a = int(input("ENTER NUMBER: "))
#     b = int(input("ENTER NUMBER: "))
#     print(a+b)

# add()
    
# #without return type & with arg

# def sub(a,b):
#     print(a-b)

# a = int(input("ENTER NUMBER: "))
# b = int(input("ENTER NUMBER: "))
# sub(a,b)

# #without arg & with return type

# def mul():
#     a = int(input("ENTER NUMBER: "))
#     b = int(input("ENTER NUMBER: "))
#     return a*b

# mul = mul()
# print(mul)

# #with arg & return

# def div(a,b):
#     return a/b

# a = int(input("ENTER NUMBER: "))
# b = int(input("ENTER NUMBER: "))

# div = div(a,b)
# print(f"{div=:.03}")

def sum_of_digits(a):
    while a != 0:
        sum = 0
        temp = a%10
        a /= 10
        sum += temp
    print(sum)

a = int(input("ENTER NUMBER: "))
sum_of_digits(a)


# a =3
# b= 3.0
# print(a+b)
# print(type(a+b))

# print(str(99))
# print(type(str(99)))


# print(bool(10))
# print(bool(0))
# print(bool("Hello"))
# print(bool([]))
# print(bool(True))

# a = 5
# b = 1
# result = a/b
# print(result)
# print(type(result))

# def greet():
#     print("Hello ")

# greet()


# def printTwice():
#     for _ in range(2):
#         print(98)
# printTwice()


#def printt(a):
#     global d
#     d =8
#     print(a)
# c=int(input("Enter no. "))
# printt(c)
# printt(8)
# print(d)

# import math
# def sum(input):
#     print(input,input)
# sum(math.cos(math.pi))
# sum(88)



# def cattwice(part1, part2):
#     global cat
#     cat = part1 + part2

# a = "abc"
# b = "de"
# cattwice(a,b)
# print(cat)

# def multiply(a,b):
#     result = a*b
#     return result
# def main():
#     x=5
#     y=4
#     produvt = multiply(x,y)
#     print (produvt)



# def number(inpu):
#     print(inpu)
# inp = input("enter the number")

# print(inp) 
# number()


# fruit ="banana"
# length = len(fruit)
# last = fruit[length-1]
# print(last)
# last = fruit[0:length]
# print (last)


# # fruit = ""
# full_name = input("Enter your full name: ")

# # Convert the name to uppercase
# upper_name = full_name.upper()
# print("Name in uppercase:", upper_name)

# # Count how many times 'a' or 'A' appears
# a_count = full_name.lower().count('a')
# print("Number of times 'a' appears:", a_count)

# # Perform slicing: first two and last two letters
# print(full_name[:2])
# print(full_name[-2:])

# def find(strng, ch):
#     index = 0
#     while index < len(strng):
#         if strng[index] == ch :
#             return index
#         index = index +1
#     return None
# a = find("python","n")
# print(a)
# fruit = "banana"
# count = 0
# for char in fruit:
#     if char == "a":
#         count +=1
# print(count)

# from string import*
# ffruit = "guava"
# index = ffruit.find("a")
# print(index)

# a = "Bsnanana"
# print(a.find("na"))
# print(a.find("na",3))
# print(a.find("a",1,3))
# import string
# def isa(ch):
#     global index
#     index = string.ascii_lowercase.find(ch)
#     return string.ascii_lowercase.find(ch) != -1
# print(isa("h"))
# print(f"index of h {index}")

# import string
# def isa(ch):
#     global index
#     index = string.ascii_lowercase.find(ch)
#     return ch in string.ascii_lowercase
# print(isa("h"))
# print(f"index of h {index}")

# import string
# def islower(ch):
#     global index 
#     index = string.ascii_lowercase.find(ch)
#     return "a"<= ch <= "z"
# x= "z"
# print(islower(x))
# print(f"Index of {x} {islower(x)}")



# r = range(1,5)
# a= list(r)
# print (a)

# r = range(1,5)
# a= [x for x in r]
# print (a)

# r = range(1,5)
# a= [*r]
# print (a)

# r = range(1,5)
# a= []
# for x in r:
#     a.append(x)
# print (a)


# def my_fun(food):
#     for x in food:
#         print(x)
# fruit = ["apple","Banana","cherry"]
# my_fun(fruit)

# list =[10,20,30,50,40,60,70]
# print(list[::3])

# horsemmen = ["war","famine","pestilence","live"]

# i = 0
# while i<4:
#     if (i==2):
#       print(horsemmen[i])
#     i=i+1

# for num in range(20):
#    if num %2 ==0:
#       print(num)


# a = [1,2,3,4,5]
# a[1:3] = ["x","y"]
# print (a)

# lis = ["a","b","c","d","f","g"]
# lis[2]=[5]
# print(lis)
# lis[1:3] = ["c","d"]
# print(lis)

# lis = ["a","b"]
# del lis[1]
# print(lis)

def tail(list):
    return list[1:]
number = [1,2,3]
rest = tail(number)
print(rest)


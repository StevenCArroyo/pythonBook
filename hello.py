from os import system


print("hello\nworld")


'''
this is
a 
multiline comment
'''

print(f"3+2 = {3+2}")
print(5>1)
num1=5
num2=10
print(num1+num2)

name = input("what's your name?: ")
print(f"hello {name*10}")

names=["steve", "nola"]
names.append("ed")
names.insert(0, "kate")
print(names)
names.remove("steve")
print(names)
names.pop(0)
print(names)

#if __name__ == main()
 # main()
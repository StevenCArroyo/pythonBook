
def fizz_buzz(i):
  if i % 3 == 0 and i % 5 == 0:
      print(f" {i} is fizz buzz")
  elif i % 3 == 0:
    print(f"{i} is fizz")
  elif i % 5 == 0:
    print(f"{i} is buzz")
  else:
    print(f"{i} is boring")

print(f"calling function",fizz_buzz(30))

"""
for i in range(1,101):
    print(f"i is: ", i)
    if i % 3 == 0 and i % 5 == 0:
      print("fizz buzz")
    elif i % 3 == 0:
      print("fizz")
    elif i % 5 == 0:
      print("buzz")
"""

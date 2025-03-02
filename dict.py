fav_pizza = {
  "john":"pepperoni",
  "steve":"sausage",
  "luna":"tuna"
}

fav_pizza["nola"] = "mushroom"

print(fav_pizza["nola"])
print(fav_pizza.keys())

for x,y in fav_pizza.items():
    print(f"key {x}  value {y}")
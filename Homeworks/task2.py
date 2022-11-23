# x = 0
# y = 1
# z = 0

print("\nДано утверждение:")
print("¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z\n")

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not (x or y or z) == (not x) and (not y) and (not z):
                print(f"x = {x}, y = {y}, z = {z} => утверждение истинно")
            else:
                print(f"x = {x}, y = {y}, z = {z} => утверждение ложно")

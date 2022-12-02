p1 = None
p2 = None

with open("task5text1.txt", "r") as file:
    p1 = file.readline()

with open("task5text2.txt", "r") as file:
    p2 = file.readline()

print(p1)
print(p2)
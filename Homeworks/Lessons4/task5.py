p1 = None
p2 = None
polynom_arr = []

with open("task5text1.txt", "r") as file:
    p1 = file.readline()

with open("task5text2.txt", "r") as file:
    p2 = file.readline()



p1arr = p1.split(" ")
p2arr = p2.split(" ")

for i in range(0, 5, 2):
    p1_mon = p1arr[i].split("x**")
    p2_mon = p2arr[i].split("x**")
    num1 = int(p1_mon[0])
    num2 = int(p2_mon[0])

    # if i > 1 and p1arr[i - 1] == "-":
    #     num1 = -num1
    # if i > 1 and p2arr[i - 1] == "-":
    #     num2 = -num2

    if i > 1:
        if p1arr[i - 1] == "-":
            num1 = -num1
        if p2arr[i - 1] == "-":
            num2 = -num2

        if num1 + num2 < 0:
            polynom_arr.append(" - ")
        else:
            polynom_arr.append(" + ")

    if i < 4:
        k1 = p1_mon[1]
        k2 = p2_mon[1]
        if k1 == k2:
            polynom_arr.append(f"{abs(num1 + num2)}x**{k1}")
        else:
            polynom_arr.append(f"({num1}x**{k1} + {num2}x**{k2})")
    else:
        polynom_arr.append(f"{abs(num1 + num2)}")



print(polynom_arr)

with open("task5sum_of_polynom.txt" , "w") as file:
    file.write("".join(polynom_arr))


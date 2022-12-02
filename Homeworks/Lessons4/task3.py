nums = []

for i in range(5):
    nums.append(int(input(f"Введите {i + 1}-е число: ")))

print(list(set(nums)))
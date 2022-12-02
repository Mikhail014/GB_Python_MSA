nums = []

for i in range(5):
    n = int(input(f"Введите {i + 1}-е число: "))
    if n not in nums:
        nums.append(n)

print(nums)
nums = []

for i in range(13):
    nums.append(int(input(f"Введите {i + 1}-е число: ")))

non_rep_elem = []

for el in nums:
    if nums.count(el) == 1:
        non_rep_elem.append(el)

print(f"Количество неповторяющихся элементов: {non_rep_elem}")
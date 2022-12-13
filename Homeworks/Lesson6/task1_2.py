### list comp
nums = [int(input(f"Введите {i + 1}-е число: ")) for i in range(7)]
### list comp
non_rep_elem = [el for el in nums if nums.count(el) == 1]

print(f"Исходный список: {nums}")
print(f"Количество неповторяющихся элементов: {non_rep_elem}")
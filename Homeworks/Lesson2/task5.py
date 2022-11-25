from random import randint

arr = [i for i in range(1, 11)]

print("Оригинальный список:")
print(arr)

rand_ind = []
len_arr = len(arr)
i = 0

while len_arr != len(rand_ind):
    r = randint(0, len_arr - 1)
    if r not in rand_ind:
        rand_ind.append(r)
        temp = arr[i]
        arr[i] = arr[r]
        arr[r] = temp
        i += 1

print("Перемешанный список:")
print(arr)
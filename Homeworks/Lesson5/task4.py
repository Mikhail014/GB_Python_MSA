data_file_comp = None
data_file_rec = None

with open("t4_in_data", "r") as file:
    data_file_comp = file.readline()

with open("t4_out_data", "r") as file:
    data_file_rec = file.readline()

def data_compression(data):
    sym = data[0]
    count = 0
    data_out = ""
    for d in data:
        if sym == d and count < 9:
            count += 1
        else:
            data_out += f"{count}{sym}"
            count = 1
            sym = d

    data_out += f"{count}{sym}"

    with open("t4_out_data", "w") as file_out:
        file_out.write(data_out)


def data_recovery(data):
    data_in = ""
    for ind, num in enumerate(data):
        if not num.isdigit():
            continue
        data_in += f"{data[ind + 1] * int(num)}"
    with open("t4_in_data", "w") as file_in:
        file_in.write(data_in)


print("Нажмите на 1, чтобы сжать данные из файла t4_in_data в t4_out_data.")
print("Или - на любую клавишу, чтобы данные из файла "
      "t4_out_data восстановить в t4_in_data")

launch = input("Ответ: ")
if launch == "1":
    data_compression(data_file_comp)
else:
    data_recovery(data_file_rec)
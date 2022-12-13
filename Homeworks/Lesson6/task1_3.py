text = None

with open("task1_text.txt", "r", encoding="utf-8") as file:
    text = file.readline()

textArr = text.split()

with open("task1_text.txt", "w", encoding="utf-8") as file:
    ### filter, lambda
    res = list(filter(lambda x: "абв" not in x, textArr))
    file.write(" ".join(res))
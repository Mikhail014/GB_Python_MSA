d = 0.001
pi = 3.141
my_pi = 1
count = 0
i = 3

while True:
      if count % 2 == 0:
            my_pi -= 1 / i
      else:
            my_pi += 1 / i

      diff = pi - round(my_pi * 4, 3)

      if d >= diff >= -d:
            print(f"{pi - round(my_pi * 4, 3)}")
            break

      count += 1
      i += 2

my_pi = round(my_pi * 4, 3)

print(f"{my_pi}")
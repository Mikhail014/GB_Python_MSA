nums = []

with open("file1", "r") as file:
    nums = file.readline().split()

### map
nums = list(map(int, nums))
res = None

### enumerate
for i, v in enumerate(nums):
    if i > 0 and nums[i] - 1 != nums[i - 1]:
        res = v - 1

print(res)
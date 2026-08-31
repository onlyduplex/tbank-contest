nums = input().split(" ")
for i in range(4):
    nums[i] = int(nums[i])

diff = nums[3] - nums[1]
if diff > 0:
    res = nums[0] + (nums[2] *(nums[3] - nums[1]))
else:
    res = nums[0]
print(res)


n = input()
nums = list(map(int, input().split()))
copy = nums.copy()

while len(nums) > 1:
    if nums[0] < nums[1]:
        nums.remove(nums[0])
    elif nums[0] > nums[1]:
        nums.remove(nums[1])

for i in range(len(copy)):
    if nums[0] == copy[i]:
        print(i+1)

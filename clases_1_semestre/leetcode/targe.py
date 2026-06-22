list = [1,2,3,4,5]

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
target = 9
print(twoSum(list, target))
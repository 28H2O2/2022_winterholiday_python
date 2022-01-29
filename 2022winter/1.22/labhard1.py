from operator import index


def twoSum(nums, target):
    for i in nums:
        for j in nums:
            if(int(i)+int(j) == target):
                if(nums.index(i) > nums.index(j)):
                    print([nums.index(i), nums.index(j)])
num = list(input("please input a number list"))
t = int(input("please input a number"))
twoSum(num, t)

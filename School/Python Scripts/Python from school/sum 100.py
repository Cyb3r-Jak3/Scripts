nums = []
while len(nums) <= 1:
    nums.append(input("Enter a number: "))
totalNum = nums[0] + nums[1]
if totalNum > 100:
    print "They add up to a big number"
else:
    print "They add up to", totalNum

    

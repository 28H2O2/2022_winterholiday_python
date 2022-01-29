def lengthOfLongestSubstring(astr):
    sum = 0
    for i in range(len(astr)):
        for j in range(i+1, len(astr)):
            if(astr[j] == astr[i]):
                break
        else:
            sum += 1
    return sum
x = input("please input a string\n")
print(lengthOfLongestSubstring(x))

# Write input array in reverse
tf = 'input.txt'
f = open(tf)
inputfile =f.read()
print(inputfile)

split_input = inputfile.split()
# We just need the second line 
# We just exclude the first element of the split_input
input_nums = split_input[1:]

#map calls int on each member of input_nums
integer_list = map(int, input_nums)
#for e in input_nums:
 #   print (e),

print (input_nums)

nums = " ".join(input_nums)
rev_input_nums=[]
i = 0 
while i < len(input_nums):
    rev_input_nums.append(input_nums[len(input_nums)-1-i])
    i = i + 1
revnums = " ".join(rev_input_nums)

print (revnums)

#quick solution
print(" ".join(input_nums[::-1]))
f.close()

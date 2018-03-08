tf = 'input.txt'
f = open(tf)
inputfile = f.read()
#print(inputfile) #prints input as it is 

split_input = inputfile.split()
#print(split_input) 

list_input = list(map(int,split_input[1:]))
print(list_input)

#You can sort 
list_input.sort()
print(list_input)

#sort in reverse
list_input.sort(reverse=True)
print(list_input)

#find the max
max_num = max(list_input)

#Will give the second element in list sorted in reverse
print("Second: ", sorted(list_input)[-2])

#Remove Max in array (!!Does not work with duplicates)
list_input.remove(max(list_input))
print(list_input)
print("2nd Element", max(list_input))

#STRAIGHTFORWARD ANSWER but 
# The sorting operation is O(n*log(n)), but finding the largest (without sorting) is linear ( O(n) ) since it takes one loop. A naive solution takes two loops: O(2n).
#use set to remove duplicates 
#This is actually also wrong
input_list = list(map(int,split_input[1:]))
input_list = list(set(input_list))
second_highest = input_list[-2]
print("Second Highest: ", second_highest)


#ELEGANT SOLUTION?
mlist = list(map(int, split_input[1:]))
z = max(mlist)
print ("mlist: ", mlist)

for e in mlist: 
  print ("e: ", e, "z: ", z)
  if e == z: 
    mlist.remove(e)
  else: 
    continue


print (mlist)
print ("Right: ", max(mlist))
######DOESNT WORK?>>


#ELEGANT SOLUTION 2
nlist = list(map(int, split_input[1:]))
print ("nlist: ", nlist)

while max(nlist) == z:
  nlist.remove(max(nlist))
print("RIGHT: ", max(nlist))

#ANOTHER ONE USING SORT
newlist = list(map(int, split_input[1:]))
print (sorted(list(set(newlist)))[-2])

f.close()

#tf = 'input.txt'
tf = input("Enter filename:")
f = open(tf)
inputfile =f.read()
print(inputfile)




split_input = inputfile.split()
#We just need the second line for the hash(tuple)
#We just include the first element of the split_input
hash_input = split_input[1:]

#map calls int on each member of the split_input
integer_list = map(int, hash_input)

#Tuple
t = tuple(integer_list)
print("tuple: ", t)

#hash
print("hash(tuple): ", hash(t))

f.close()

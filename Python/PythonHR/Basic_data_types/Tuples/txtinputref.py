#tf = 'input.txt'
tf = input("Enter filename:")
f = open(tf)
inputfile =f.read()
print(inputfile)
inputcmd = f.readlines()[1:]

#Reading per line
print("last line: ", inputcmd)
lines = [line.rstrip('\n') for line in open(tf)]
lastnlines = lines[1:] 
print("lines: ", lines)
print("lastnlines:", lastnlines)



split_input = inputfile.split()
print("split_input ", split_input)
print("split_input entry: ", split_input[1:])

#map calls int on each member of the split_input
integer_list = map(int, split_input[1:])
print(integer_list)
print("integer_list: ", list(integer_list))

#Tuple
t = tuple(integer_list)
print("tuple: ", t)

#hash
print("hash(tuple): ", hash(t))

f.close()

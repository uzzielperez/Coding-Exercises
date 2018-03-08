tf = input("Enter filename: ")
f = open(tf)

lines = [line.rstrip('\n') for line in open(tf)]
print("lines ", lines)

input_list = list(map(int, lines)) 
#print("input_list ", input_list)
x = input_list[0]
y = input_list[1]
z = input_list[2]
n = input_list[3]

print ([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k)!=n)])


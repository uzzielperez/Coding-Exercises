tf = input("Enter filename: ")
f = open(tf)
inputfile = f.read()

split_input = inputfile.split()
#print(split_input)


#for i in range(len(split_input)): #len(list) is list.size() 
  #print (i, split_input[i])

#############STILL MASSAGING THE INPUT################
#new way

with open(tf) as g:
  table_data = [line.split() for line in g]

#print (table_data)

size = 2

new_input = split_input[1:]
students = [new_input[i:i+size] for i  in range(0, len(new_input), size)]
#print(students)

#############PROCESSING THE INPUT#####################
#Sorting, I guess a-z
#students.sort()
#print(students)

#Sorting according to element of each list
#We want to sort by comparing 2nd elements
#students.sort(key=lambda x: x[1])
#print(students)

students_list = sorted(students, key=lambda x:x[1])
#max_num = max(students_list, key=lambda x:x[1])
#print("max score: ", max_num)
min_num = min(students_list, key=lambda x:x[1])
#print (min_num)
while  min(students_list, key=lambda x:x[1])[1] == min_num[1]:
  students_list.remove( min(students_list, key=lambda x:x[1])) 

newmin =  min(students_list, key=lambda x:x[1])

second_lowest = []
for e in students_list:
  #print (e[0], e[1])
  if e[1]==newmin[1]:
    second_lowest.append(e[0])
  else:
    continue
second_lowest.sort()
print ("People 2nd lowest: ",second_lowest)
for i in second_lowest:
  print (i)

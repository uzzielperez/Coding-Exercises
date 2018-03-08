
#input_list.pop(0) #removes first element of a list
#new_input = input_list[1:]
#size = 4
#student_scores = [new_input[i:i+size] for i in range(0,len(new_input),size)]
#student_scores = student_scores[:-1]
#num_students = len(student_scores)
#print(student_scores)

#rel_student = student_scores[num_students-1]
#print(rel_student)

#ave = (float(rel_student[1])+float(rel_student[2])+float(rel_student[3]))/3.00
#print("%.2f" % ave)

with open("input.txt","r") as ins:
  array = []
  for line in ins:
    array.append(line)

#print (array)
with open("input.txt") as f:
      content = f.readlines()
#print(content)

fp = open('input.txt') # open file on read mode
lines = fp.read().split("\n") # create a list containing all lines
#print(lines)



fp.close()

##### WHAT WE NEED
fname = open("input.txt")
line_2 = fname.read()
newlist = line_2.splitlines()
print (newlist)

n =int(newlist[0])
#Start a dictionary
#https://stackoverflow.com/questions/3765533/python-array-with-string-indices

student_marks={}
for i in range(n):
  line = newlist[i+1].split()
  name, scores = line[0], line[1:]
  scores = list(map(float,scores))
  #scores = list(map(float,line))
  #student_marks[name] = scores
  student_marks[name] = scores
  print(i,line, name, scores, student_marks)

query_name = newlist[len(newlist)-1] 
print (query_name)  
query_scores = student_marks[query_name]
print (query_scores)

sum_scores = sum(query_scores)
avg = sum_scores/len(query_scores)
print("%.2f" % avg)

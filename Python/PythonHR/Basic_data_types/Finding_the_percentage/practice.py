tf = input("Enter filename: ",)
f = open(tf)
input_file = f.read()
print(input_file)

input_list = input_file.split()
print(input_list)

#input_list.pop(0) #removes first element of a list
new_input = input_list[1:]
size = 4
student_scores = [new_input[i:i+size] for i in range(0,len(new_input),size)]
student_scores = student_scores[:-1]
num_students = len(student_scores)
print(student_scores)

rel_student = student_scores[num_students-1]
print(rel_student)

ave = (float(rel_student[1])+float(rel_student[2])+float(rel_student[3]))/3.00
print("%.2f" % ave)

#https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points

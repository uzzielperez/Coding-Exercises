#In Python3.x and Python 2 you cannot input multiline strings for that purpose you would need to get input from the user line by line and then .join() 
#them using \n, or you can also take various lines and concatenate them using + operator separated by \n

# https://stackoverflow.com/questions/30239092/how-to-get-multiline-input-from-user

#Here's one way to do it
#Typed input 

lines = []
line = input('First line: ')
while line:
    lines.append(line)
    line = input('Next line: ')
print(lines)


#If you get the input from some source all at once, you can use

#the_input.split('\n')

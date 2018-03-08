#tf = 'input.txt'
tf = input("Enter filename:")
f = open(tf)
inputfile =f.read()
print(inputfile)
inputcmd = f.readlines()[1:]

list = []
num_lines = sum(1 for line in open(tf))

print (num_lines)

lines = [line.rstrip('\n') for line in open(tf)]
lastnlines = lines[1:]
print("lines: ", lines)
print("lastnlines:", lastnlines)
print (range(num_lines))

print ("Input cmd",inputcmd)

for element in lastnlines:
        s = element.split() #splits a line of the input into word/smaller elements
        # print (s)
        cmd = s[0]
        #print ("cmd:", cmd)
        args = s[1:] #arguments of the command are the last 2 entries

        if cmd !="print":
            cmd += "(" + ",".join(args) +")" #cmd("arg", "arg") or #cmd()
            #print ("cmd:", cmd)
            eval("list."+cmd) #executes the list.cmd(args)
        else:
            print (list)


f.close()

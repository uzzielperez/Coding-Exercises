if __name__ == '__main__':
    N = int(input()) #Just the number of commands 
    list = []
    
    for element in range (N):
        s = input().split() #splits an input line into smaller elements and puts them in a list
        cmd = s[0] #the name of the command would be the first word, i.e. reverse, print
        args = s[1:] #arguments of the command excludes the first word
        if cmd !="print":         
            cmd += "(" + ",".join(args) +")"
            eval("list."+cmd)
        else:
            print (list)
        

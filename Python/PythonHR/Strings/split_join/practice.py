tf = "input.txt"
f = open(tf)
txt = f.read()
txtlist = txt.split()
print ("txtlist: ", txtlist)


# :/ s=raw_input() x=[] for i in s: if i.isupper(): i=i.lower() x.append(i) else: i=i.upper() x.append(i) str1=''.join(x) print str1

x=[]
with open(tf) as fileobj:
    for line in fileobj:  
       for ch in line: 
         if ch.isupper()==True:
           ch=ch.lower()
           x.append(ch)
         else:
           ch=ch.upper()
           x.append(ch)
str1="".join(x)
print(str1)



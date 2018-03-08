y =int(input("Enter year: "))

def is_leap(y):
  if y%4 !=0: 
    leap = False 
  elif y%4 ==0:
    if y%100 !=0: 
      leap = True
    elif y%100==0 and y%400==0: 
      leap = True
    elif y%100==0 and y%400 !=0: 
      leap = False
  return leap 

print (is_leap(y))

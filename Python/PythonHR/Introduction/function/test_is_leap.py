def is_leap(year):
    if year%4 !=0: 
        leap = False
    elif year%4 == 0: 
        if year%100 !=0: 
            leap = True
        elif year%100 ==0: 
            if year%400==0: 
                leap = True
            elif year%400 !=0: 
                leap = False
    # Write your logic here
    
    return leap

def test_is_leap():
  year_is = is_leap(1992)
  assert year_is == True 

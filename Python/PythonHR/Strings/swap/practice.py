tf = "input.txt"
f = open(tf)
txt = f.read()
def swap_case(s):
  swptxt = s.swapcase()
  return swptxt

print (txt)
print (swap_case(txt))

f.close()

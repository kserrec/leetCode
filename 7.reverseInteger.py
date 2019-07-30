def reverseInt(x):
  # make into int
  s = str(x)
  isNegative = False
        
  # if negative
  if s[0] == '-':
    s = s[1:]
    isNegative = True
            
  # reverse string
  s = s[::-1]
        
  # remove preceding zeroes
  for char in s:
    if char == '0':
      s = s[1:]
    else:
      break
                
  # print with negative sign if negative
  if isNegative:
    s = "-" + s
        
  # if empty, return 0
  if s == '':
    return 0

  # turn s to int
  s = int(s)
        
  # if s out of range, return 0
  if s >= 2147483647 or s <= -2147483648:
    return 0
        
  return s

# test cases
print(reverseInt(000))
print(reverseInt(2147483647))
print(reverseInt(-854))
print(reverseInt(120))
print(reverseInt(-134))
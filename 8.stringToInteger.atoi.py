def atoi(s):
  # check if nothing
  if s == "":
    return 0

  # discard whitespace
  for char in s:
    if char == " ":
      s = s[1:]
    else:
      break
  
  # check if neg
  isNegative = False
  if s[0] == '-':
    isNegative = True
    s = s[1:]
  
  # remove trailing nondigits
  digList = ['0','1','2','3','4','5','6','7','8','9']
  for i in range(len(s)):

    # check if digit in order to remove trailing non-num chars
    isNum = False
    for dig in digList:
      if s[i] == dig:
        isNum = True
        break

    # remove trailing non-num chars
    if isNum == False:
      s = s[:i]
      break
    
  # if negative, add minus sign
  if isNegative:
    s = '-' + s

  # if nothing or just dash, return 0
  if s == "" or s == "-":
    return 0

  # convert to int
  s = int(s)

  # make sure within range
  if s <= -2147483648:
    return -2147483648
  if s > 2147483647:
    return 2147483647
  
  return s

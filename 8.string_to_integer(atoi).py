def myAtoi(strin):
        # check if nothing
        if strin == "":
            return 0
        
        # reassign
        s = strin
        
        # discard whitespace
        for char in s:
            if char == " ":
                s = s[1:]
            else:
                break
                
        # check if discarding whitespace emptied it
        if s == "":
            return 0   
        
        # check if neg or pos
        hasNegative = False
        if s[0] == '-':
            hasNegative = True
            s = s[1:]
        elif s[0] == "+":
            hasPositive = True
            s = s[1:]
            
        # check if was only pos or neg sign
        if s == "":
            return 0 
            
        digList = ['0','1','2','3','4','5','6','7','8','9']
        # check if starts with dig
        startsWithDig = False
        for dig in digList:
            if s[0] == dig:
                startsWithDig = True
        if startsWithDig == False:
            return 0
        
        # remove trailing nondigits
        for i in range(len(s)):

            # check if digit to remove trailing non-num chars
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
        if hasNegative:
            s = '-' + s

        # if nothing or just dash, return 0
        if s == "" or s == "-":
            return 0
        
        # convert to int
        s = int(s)

        # make sure within range
        if s < -2147483648:
            return -2147483648
        if s > 2147483647:
            return 2147483647

        return s

print(myAtoi("  -45"))
print(myAtoi("+-"))
print(myAtoi("  "))

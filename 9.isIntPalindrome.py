def isIntPalindrome(x):
    # do so without string conversion!

    # check if negative
    if x < 0:
        return False

    # check if single digit
    if x < 10:
        return True

    # check if 2 digits
    if x < 100:
      if x % 11 == 0:
        return True
      else:
        return False

    # check if more digits
    # first make some functions to deal with this

    # get length of integer
    def intLength(y):
        n = 0
        while y > 1:
            y = y / 10
            n = n + 1
        return n

    # formula for nth term from the right (except for zeroth)
    def formula(n, i):
        return ((n - (n%(10**i)))//10**i)%10

    # arr for holding values
    arr = []

    # get zeroth element
    arr.append(x%10)

    # loop through to grab each term from right to left
    for i in range(1,intLength(x)):
      arr.append(formula(x,i))

    # reverse arr
    revArr = arr[::-1]

    # assume is palindrome
    # loop through half of arr comparing arr with revArr to check assumption
    #   return False if False, otherwise return True
    def isPalindrome(arr, revArr):
        for i in range(len(arr)//2):
            if arr[i] != revArr[i]:
                return False
        return True

    return isPalindrome(arr, revArr)

print(isIntPalindrome(10))
        

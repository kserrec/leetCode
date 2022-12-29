def conversion(s, numRows):
  def makeGrid(s, numRows):
          downState = False
          length = len(s)
          grid = [[0] * length for i in range(numRows)]
          i = 0  # row
          j = 0  # column
          for k in range(length):
              m = i
              n = j
              if (m == (numRows - 1)) or m == 0:
                  downState = not downState
              if downState:
                  i = i + 1
              else: 
                  i = i - 1
                  j = j + 1
              grid[m][n] = s[k]
          return grid

  def makeResultStringFromGrid(grid):
    resultString = ""
    for arr in grid:
      for char in arr:
        if not char == 0:
          resultString = resultString + char
    return resultString

  # trivial case
  if numRows == 1: 
    return s
    
  # otherwise
  return makeResultStringFromGrid(makeGrid(s, numRows))
        

print(conversion("paypalishiring", 3))



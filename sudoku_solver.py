grid = [[0,0,2,0,1,7,0,4,0],
        [0,6,0,0,0,0,0,0,2],
        [0,0,0,0,3,0,0,0,0],
        [0,0,0,5,0,0,0,0,0],
        [0,0,6,0,2,4,0,1,0],
        [8,0,0,0,0,0,9,0,0],
        [0,0,0,6,0,0,0,5,0],
        [0,9,0,0,7,5,1,0,0],
        [0,0,7,3,0,0,0,0,0]]

def printSudu(su):
    for i in range(len(su)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(su[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(su[i][j])
            else:
                 print(str(su[i][j]) + " ", end="")

#recursive backtracking

def possi(row, column, number):
    global grid
    # row
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    # column
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    
    # square
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False

    return True

def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possi(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                return
                
      
    printSudu(grid)
    input('More possible solutions are')

solve()

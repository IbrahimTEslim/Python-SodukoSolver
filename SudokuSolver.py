import numpy as np

l1=[0,0,0,0,0,0,0,0,0]
l2=[0,0,0,0,0,0,0,0,0]
l3=[0,0,0,0,0,0,0,0,0]
l4=[0,0,0,0,0,0,0,0,0]
l5=[0,0,0,0,0,0,0,0,0]
l6=[0,0,0,0,0,0,0,0,0]
l7=[0,0,0,0,0,0,0,0,0]
l8=[0,0,0,0,0,0,0,0,0]
l9=[0,0,0,0,0,0,0,0,0]


def possible(y, x, n):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print np.matrix(grid)
    raw_input("More?")


print"Insert your sudoku line by line with comma between the numbers  Ex: \"1,0,0,5,9,8,4,6,7\""
l1 = input("First Line: ")
l2 = input("Second Line: ")
l3 = input("Third Line: ")
l4 = input("4th Line: ")
l5 = input("5th Line: ")
l6 = input("6th Line: ")
l7 = input("7th Line: ")
l8 = input("8th Line: ")
l9 = input("9th Line: ")


grid = [[l1[0], l1[1], l1[2], l1[3], l1[4], l1[5], l1[6], l1[7], l1[8]],
        [l2[0], l2[1], l2[2], l2[3], l2[4], l2[5], l2[6], l2[7], l2[8]],
        [l3[0], l3[1], l3[2], l3[3], l3[4], l3[5], l3[6], l3[7], l3[8]],
        [l4[0], l4[1], l4[2], l4[3], l4[4], l4[5], l4[6], l4[7], l4[8]],
        [l5[0], l5[1], l5[2], l5[3], l5[4], l5[5], l5[6], l5[7], l5[8]],
        [l6[0], l6[1], l6[2], l6[3], l6[4], l6[5], l6[6], l6[7], l6[8]],
        [l7[0], l7[1], l7[2], l7[3], l7[4], l7[5], l7[6], l7[7], l7[8]],
        [l8[0], l8[1], l8[2], l8[3], l8[4], l8[5], l8[6], l8[7], l8[8]],
        [l9[0], l9[1], l9[2], l9[3], l9[4], l9[5], l9[6], l9[7], l9[8]]]


#if len(l1) or len(l2) or len(l3) or len(l4) or len(l5) or len(l6) or len(l7) or len(l8) or len(l9) !=9:
#    print "\n Error in inputting line numbers!!"
#else:
solve()

raw_input("\n\nFinish!")
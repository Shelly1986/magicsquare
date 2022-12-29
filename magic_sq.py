magic_square = []
magic_square.append([2,7,6])
magic_square.append([9,5,1])
magic_square.append([4,3,8])
n = len(magic_square)
def display():
    for row in magic_square:
        print(row)

def check():
    sum_d1 = 0
    sum_d2 = 0
    for row in range(3):
        sum_d1 += magic_square[row][row]

    for i in range(3):
        sum_d2 += magic_square[i][n-i-1]
    if not(sum_d1 == sum_d2):
        return "Not a magic square"
    
    for row in range(0,3):
        sum_rows = 0
        sum_columns = 0
        for col in range(0,3):
            sum_rows += magic_square[row][col]
            sum_columns += magic_square[col][row]
        if not(sum_rows == sum_columns == sum_d1):
            return "Not a magic square"
    
    
    return "It is a magic square"
        
display()
print(check())



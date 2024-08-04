def check_number(matrix):
    for row in matrix:
        for i in row:
            if not isinstance(i, (int, float)):
                return False
    return True

def addition(matrix1, matrix2, num_row, num_col):
    result = []
    for i in range(num_row):
        row = []
        for j in range(num_col):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

while True:
    row1 = int(input("Enter Number of Rows for 1st Matrix: "))
    col1 = int(input("Enter Number of Columns for 1st Matrix: "))
    row2 = int(input("Enter Number of Rows for 2nd Matrix: "))
    col2 = int(input("Enter Number of Columns for 2nd Matrix: "))
    if row1 == row2 and col1 == col2:
        break
    else:
        print("The dimensions of the two matrices must be the same. Please try again.")

matrix1 = []
matrix2 = []
print("Enter values for 1st matrix: ")
for i in range(row1):
    row = []
    for j in range(col1):
        value = int(input(f"Value at row {i} and col {j}: "))
        row.append(value)
    matrix1.append(row)

print("Enter values for 2nd matrix: ")
for i in range(row2):
    row = []
    for j in range(col2):
        value2 = int(input(f"Value at row {i} and col {j}: "))
        row.append(value2)
    matrix2.append(row)

if not check_number(matrix1):
    print("Non-numeric values in 1st matrix.")
elif not check_number(matrix2):
    print("Non-numeric values in 2nd matrix.")
else:
    print("Result: ")
    result_matrix = addition(matrix1, matrix2, row1, col1)
    for row in result_matrix:
        print(row)

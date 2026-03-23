def print_matrix(matrix, title):
    print(title)
    for row in matrix:
        print(row)
    print()


def main():
    #student id: 2585070
    d1 = 0
    d2 = 7
    k = 5
    shift = -7
    rows_keep = 2

    matrix = [
        [21, 22, 23, 24],
        [25, 26, 27, 28],
        [29, 30, 31, 32]
    ]

    print_matrix(matrix, "Original matrix:")

    print("Specific element matrix[1][2]:", matrix[1][2])
    print("First two rows:", matrix[:2])

    first_column = [row[0] for row in matrix]
    print("First column:", first_column)

    upper_left_2x2 = [row[:2] for row in matrix[:2]]
    print("Upper-left 2x2 sub-array:", upper_left_2x2)

    row_index = d1 % len(matrix)
    col_index = d2 % len(matrix[0])

    for j in range(len(matrix[row_index])):
        matrix[row_index][j] += shift

    for i in range(len(matrix)):
        matrix[i][col_index] *= k

    print_matrix(matrix, "Modified matrix:")

    sub_array = [row[:k] for row in matrix[:rows_keep]]
    print("Sub-array using first rows_keep rows and first k columns:")
    for row in sub_array:
        print(row)


if __name__ == "__main__":
    main()

#What happened here
#	row_index = 0 % 3 = 0 â†’ modify first row
#	col_index = 7 % 4 = 3 â†’ modify fourth column
#   add shift = -7 to row 0
#	multiply column 3 by k = 5
#Modified matrix result
#[
#    [14, 15, 16, 85],
#    [25, 26, 27, 140],
#    [29, 30, 31, 160]
#]
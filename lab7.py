
#Student ID = 2585070
#d1 = 0
#d2 = 7
#k = (0 + 7) % 4 + 2 = 5
#shift = 0 - 7 = -7
#rows_keep = (0 % 2) + 2 = 2
#So all personalized outputs below use:
#k = 5
#shift = -7
#rows_keep = 2
#
def print_matrix(matrix, title):
    print(title)
    for row in matrix:
        print(row)
    print()


def main():
    d1 = 0
    d2 = 7
    k = 5
    shift = -7
    rows_keep = 2

    matrix = [
        [5, 10, 15, 20, 25],
        [30, 35, 40, 45, 50]
    ]

    print_matrix(matrix, "Original rectangular matrix:")

    print("Dimensions:")
    print("Rows =", len(matrix))
    print("Columns =", len(matrix[0]))

    last_column = [row[-1] for row in matrix]
    print("Last column:", last_column)

    first_3_cols = [row[:3] for row in matrix]
    print("All rows, first 3 columns:")
    for row in first_3_cols:
        print(row)

    chosen_row = d1 % len(matrix)
    old_row = matrix[chosen_row][:]
    new_row = [value + k for value in old_row]
    matrix[chosen_row] = new_row

    start_col = d2 % 2
    sliced_subarray = [row[start_col:] for row in matrix]

    print("\nChosen row index:", chosen_row)
    print("Old row:", old_row)
    print("New row:", new_row)

    print_matrix(matrix, "Matrix after row replacement:")

    print("Sliced sub-array from starting column", start_col)
    for row in sliced_subarray:
        print(row)


if __name__ == "__main__":
    main()

#What happened here
#	chosen_row = 0 % 2 = 0 â†’ first row replaced
#	add k = 5 to that row
#	start_col = 7 % 2 = 1
#New first row
#[10, 15, 20, 25, 30]
# Function 1: Lists - Removing Duplicates and Sorting
def remove_duplicates_and_sort(numbers):
    # Step 1: Create a new list and only add items if they aren't already in it
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
            
    # Step 2: Sort the unique list from smallest to largest
    unique_list.sort()
    
    return unique_list

# Function 2: Single-Dimensional Arrays - Cumulative Sum
def cumulative_sum(arr):
    result_list = []
    current_sum = 0
    
    # Keep a running total and append it to our new list on every loop
    for number in arr:
        current_sum = current_sum + number
        result_list.append(current_sum)
        
    return result_list

# Function 3: Slicing - Extracting Every Nth Element
def slice_every_nth(lst, step):
    result_list = []
    
    # Use range(start, stop, step) to jump through the list indexes
    for i in range(0, len(lst), step):
        result_list.append(lst[i])
        
    return result_list

# Function 4: Arithmetic Operations with Arrays - Dot Product
def dot_product(list1, list2):
    total = 0
    
    # Loop through the indexes and multiply the elements at the same position
    for i in range(len(list1)):
        total = total + (list1[i] * list2[i])
        
    return total

# Function 5: Arithmetic Operations with Arrays - Matrix Multiplication
def matrix_multiplication(matrix1, matrix2):
    # Find the dimensions of the matrices
    rows_m1 = len(matrix1)
    cols_m1 = len(matrix1[0])
    cols_m2 = len(matrix2[0])
    
    # Step 1: Create an empty result matrix filled with zeros using basic loops
    result = []
    for i in range(rows_m1):
        empty_row = []
        for j in range(cols_m2):
            empty_row.append(0)
        result.append(empty_row)
        
    # Step 2: Calculate the matrix multiplication
    for i in range(rows_m1):
        for j in range(cols_m2):
            for k in range(cols_m1):
                # Multiply the matching row and column elements and add to the running total
                result[i][j] = result[i][j] + (matrix1[i][k] * matrix2[k][j])
                
    return result


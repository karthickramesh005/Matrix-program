# Get Matrix input from user  in Python :


r = int(input("Enter the number of rows: "))
c= int(input("Enter the number of columns: "))
# Use list comprehensions to get the matrix elements
a = [[int(input(f"Enter element at position ({i+1}, {j+1}): ")) for j in range(c)] for i in range(r)]
print(a)

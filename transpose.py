#transpose

# Original matrix
m=[[1, 2, 3],[4, 5, 6]]

# Transpose using list comprehension
t=[[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

# Print result
for row in t:
    print(row)

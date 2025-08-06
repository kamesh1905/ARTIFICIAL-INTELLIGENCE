def set_operations_demo():
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}
    return {
        "Union": A | B,
        "Intersection": A & B,
        "Difference": A - B,
        "Symmetric Difference": A ^ B
    }
s=set_operations_demo()
print(s)

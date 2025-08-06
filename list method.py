def list_methods_demo():
    lst = [1, 2, 3]
    lst.append(4)
    lst.extend([5, 6])
    lst.insert(0, 0)
    del lst[2]
    return lst
r=list_methods_demo()
print(r)

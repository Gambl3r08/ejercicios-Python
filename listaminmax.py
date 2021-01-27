def min_max(lst):
    lst.sort()
    orden = []
    orden.append(lst[0])
    lst.sort(reverse=True)
    orden.append(lst[0])
    return(orden)

lst = [1, 4, 6 ,8, 3, 7]

min_max(lst)
def merge_sorted_lists(a: list[int | float], b: list[int | float]) -> list[int | float]:
    
    res = []
    i = len(a) - 1
    j = len(b) - 1
    
    while i >= 0 and j >= 0:
        
        if a[i] >= b[j]:
            res.append(a[i])
            i -= 1
        else:
            res.append(b[j])
            j -= 1
    res.append(a[0] if a[0] < b[0] else b[0])

    
    return res

a = [1,3,7,9,25,124,300,1000,1313514]
b = [2,5,23,64,127, 89789, 328748374, 398490830948984388, 93838848588484848]


print(merge_sorted_lists(a, b))

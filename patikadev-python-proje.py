l = [[1, 2], [3, 4], [5, 6, 7]]

z = []
for e in l:
    a = e[::-1] 
    z.append(a)
    y = z[::-1]

print(y)


m = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

new_m = []
for a in m:
    if isinstance(a,list):
        new_m.extend(a)
    else:
        new_m.append(a)
        
print(new_m)

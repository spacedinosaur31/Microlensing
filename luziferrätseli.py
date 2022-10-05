prim = []
for x in range(2, 99):
    count = []
    for i in range(2, x-1):
        if x % i == 0:
            count.append(1)
    if len(count) == 0:
        prim.append(x)
print(prim)


sums = []
# Hier hat es einen Fehler: Beispiel: 16 + 13 = 3 + 26, also sollte 29 nicht in der Liste vorkommen, tut sie aber.
for i in range(4, 198):
    count = []
    for x in prim:
        for y in prim:
            if x + y == i:
                count.append(1)
            if x + x**2 == i:
                count.append(1)
    if len(count) == 0:
        sums.append(i)
print(sums)    




pairsx = []
pairsy = []
sums2 = []
for x in range(2, 20):
    for y in range(2, 20):
        count = []
        if (x not in prim) or (y not in prim):
            if y != x**2:
                if x + y in sums:
                    forbiddensum = x + y
                    product = x * y
                    for t in range(2, product):
                        for w in range(2, product):
                            if t * w == product:
                                if t + w in sums:
                                    count.append(1)
                                    #print("found something:")
                                    
                            
        if len(count) == 2:
            sums2.append(x+y)
            pairsx.append(x)
            pairsy.append(y)
            
for x in sums2:
    if sums2.count(x) == 2:
        print(pairsx[sums2.index(x)], pairsy[sums2.index(x)])
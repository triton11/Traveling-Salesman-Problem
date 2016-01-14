#combos
import random
import math
combo = 0
combo_list = []
combo_list.append('01234')
for i in range(0, 2000):

    a = random.randrange(0,5)
    b = random.randrange(0,5)
    c = random.randrange(0,5)
    d = random.randrange(0,5)
    e = random.randrange(0,5)
    

    while b == a:
        b = random.randrange(0,5)
    while c == b or c == a:
        c = random.randrange(0,5)
    while d == c or d == b or d == a:
        d = random.randrange(0,5)
    while e == d or e == c or e == b or e == a:
        e = random.randrange(0,5)
   

    sequence = str(a) + str(b) + str(c) + str(d) + str(e)

    for item in combo_list:
        if item == sequence:
            combo = 0
            break
        else:
            combo += 1
    if combo == len(combo_list):
        combo_list.append(sequence)
        combo = 0
    combo = 0

print (combo_list)
print (len(combo_list))
print (combo)

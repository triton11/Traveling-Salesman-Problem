#Salesman
import pygame
import random
import math

shortest = 1000.0
v_change = 0
v_keep = 0
distance_list = []
total = 0

point_list = []

for i in range(0,5):
    point_x = random.randrange(0, 100)
    point_y = random.randrange(0, 100)
    point_list.append((point_x, point_y))



test_list = ([0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4])

list_zero = ([5,5],[0,1],[0,2],[0,3],[0,4])
list_one = ([1,0],[5,5],[1,2],[1,3],[1,4])
list_two = ([2,0],[2,1],[5,5],[2,3],[2,4])
list_three = ([3,0],[3,1],[3,2],[5,5],[3,4])
list_four = ([4,0],[4,1],[4,2],[4,3],[5,5])

test_listed = list_zero + list_one + list_two + list_three + list_four

for i in test_listed:
    if i[0] == 5 or i[1] == 5:
        distance = 100000
        distance_list.append(distance)
    else:
        x = i[0]
        y = i[1]
        distance = ((int(point_list[x][1])-int(point_list[y][1]))**2+(int(point_list[x][0])-(int(point_list[y][0])))**2)
        distance = distance**(1/2)
        distance_list.append(distance)

count = -1
for i in distance_list:
    count += 1
    if int(i) <= shortest:
        shortest = i
        next_num = count

total += shortest
v_keep = test_listed[next_num][0]
v_change = test_listed[next_num][1]
for i in list_zero:
    if i[0] == v_change or i[1] == v_change:
        i[0] = 5
        i[1] = 5
for i in list_one:
    if i[0] == v_change or i[1] == v_change:
        i[0] = 5
        i[1] = 5
for i in list_two:
    if i[0] == v_change or i[1] == v_change:
        i[0] = 5
        i[1] = 5
for i in list_three:
    if i[0] == v_change or i[1] == v_change:
        i[0] = 5
        i[1] = 5
for i in list_four:
    if i[0] == v_change or i[1] == v_change:
        i[0] = 5
        i[1] = 5


if v_keep == 0:
    test_listed = list_zero
if v_keep == 1:
    test_listed = list_one
if v_keep == 2:
    test_listed = list_two
if v_keep == 3:
    test_listed = list_three
if v_keep == 4:
    test_listed = list_four

distance_list = []
shortest = 10000


for i in test_listed:
    if i[0] == 5 or i[1] == 5:
        distance = 100000
        distance_list.append(distance)
    else:
        x = i[0]
        y = i[1]
        distance = ((int(point_list[x][1])-int(point_list[y][1]))**2+(int(point_list[x][0])-(int(point_list[y][0])))**2)
        distance = distance**(1/2)
        distance_list.append(distance)

count = -1
for i in distance_list:
    count += 1
    if int(i) <= shortest:
        shortest = i
        next_num = count



total += shortest
v_keep = test_listed[next_num][1]
v_change = test_listed[next_num][0]
for i in list_zero:
    if i[0] == v_change or i[1] == v_change:
        i[0] = 5
        i[1] = 5
for i in list_one:
    if i[0] == v_change or i[1] == v_change:
        i[0] = 5
        i[1] = 5
for i in list_two:
    if i[0] == v_change or i[1] == v_change:
        i[0] = 5
        i[1] = 5
for i in list_three:
    if i[0] == v_change or i[1] == v_change:
        i[0] = 5
        i[1] = 5
for i in list_four:
    if i[0] == v_change or i[1] == v_change:
        i[0] = 5
        i[1] = 5

if v_keep == 0:
    test_listed = list_zero
if v_keep == 1:
    test_listed = list_one
if v_keep == 2:
    test_listed = list_two
if v_keep == 3:
    test_listed = list_three
if v_keep == 4:
    test_listed = list_four

distance_list = []
shortest = 10000

for i in test_listed:
    if i[0] == 5 or i[1] == 5:
        distance = 100000
        distance_list.append(distance)
    else:
        x = i[0]
        y = i[1]
        distance = ((int(point_list[x][1])-int(point_list[y][1]))**2+(int(point_list[x][0])-(int(point_list[y][0])))**2)
        distance = distance**(1/2)
        distance_list.append(distance)

count = -1
for i in distance_list:
    count += 1
    if int(i) <= shortest:
        shortest = i
        next_num = count

total += shortest

v_keep = test_listed[next_num][1]
v_change = test_listed[next_num][0]
for i in list_zero:
    if i[0] == v_change or i[1] == v_change:
        i[0] = 5
        i[1] = 5
for i in list_one:
    if i[0] == v_change or i[1] == v_change:
        i[0] = 5
        i[1] = 5
for i in list_two:
    if i[0] == v_change or i[1] == v_change:
        i[0] = 5
        i[1] = 5
for i in list_three:
    if i[0] == v_change or i[1] == v_change:
        i[0] = 5
        i[1] = 5
for i in list_four:
    if i[0] == v_change or i[1] == v_change:
        i[0] = 5
        i[1] = 5

if v_keep == 0:
    test_listed = list_zero
if v_keep == 1:
    test_listed = list_one
if v_keep == 2:
    test_listed = list_two
if v_keep == 3:
    test_listed = list_three
if v_keep == 4:
    test_listed = list_four

distance_list = []
shortest = 10000

for i in test_listed:
    if i[0] == 5 or i[1] == 5:
        distance = 100000
        distance_list.append(distance)
    else:
        x = i[0]
        y = i[1]
        distance = ((int(point_list[x][1])-int(point_list[y][1]))**2+(int(point_list[x][0])-(int(point_list[y][0])))**2)
        distance = distance**(1/2)
        distance_list.append(distance)

count = -1
for i in distance_list:
    count += 1
    if int(i) <= shortest:
        shortest = i
        next_num = count


total += shortest
print (total)


#Crunch Time

test_this = '01243'
this_list = []
shortest = 10000
total_list = ['01234', '01243', '10423', '42013', '24103', '23410', '21304', '42301', '34102', '23041', '24301', '24031', '24130', '23401', '30214', '13402', '34012', '02341', '01432', '34021', '03412', '03214', '31024', '32014', '41302', '41203', '12034', '14302', '31204', '04123', '14023', '02431', '04321', '31420', '42103', '12304', '21340', '20431', '21034', '32041', '24310', '43021', '30142', '31240', '43120', '03124', '23014', '42130', '04312', '21043', '41032', '14230', '41320', '02143', '04213', '43210', '02134', '41023', '12340', '34201', '01324', '20134', '40213', '13240', '32410', '32401', '30241', '13024', '04132', '20314', '40231', '20143', '03241', '21430', '12430', '30421', '03142', '02314', '23104', '40312', '04231', '10234', '14032', '10342', '43201', '10324', '14203', '13204', '23140', '40321', '21403', '20341', '01342', '31402', '12043', '13420', '31042', '14320', '20413', '40123', '10432', '43012', '41230', '43102', '24013', '13042', '01423', '42031', '10243', '02413', '40132', '32104', '32140', '12403', '30124', '34120', '30412', '34210', '03421', '42310']

distance = 0
for item in total_list:
    test_this = item
    distance = 0
    for item in range(0,4):
        x = item
        new_x = int(test_this[x])
        next_x = int(test_this[x+1])
        distance += ((int(point_list[new_x][1])-int(point_list[next_x][1]))**2+(int(point_list[new_x][0])-(int(point_list[next_x][0])))**2)**(1/2)
    this_list.append(distance)
for item in this_list:
    if item <= shortest:
        shortest = item

print (shortest)

# dz_1_2. list of values in cube
cube_odd = []
for i in range(1, 1000, 2):
    cube_odd.append(i ** 3)
#print(cube_odd)
sum_numbers = 0
#i = 0
for i in cube_odd:
    sum_number = 0
    number = i
    while number:                   # by ariphmetics
        sum_number += number % 10
        number = number // 10
#    for j in str(i):               by list
#        sum_number += int(j)
    if sum_number % 7 == 0:
        sum_numbers += i
print(sum_numbers)
# exercise B
for i in range(len(cube_odd)):
    cube_odd[i] = cube_odd[i] + 17
sum_numbers = 0
for i in cube_odd:              # расчет кубов в новом списке
    sum_number = 0
    number = i
    while number:
        sum_number += number % 10
        number = number // 10
    if sum_number % 7 == 0:
        sum_numbers += i
print(sum_numbers)

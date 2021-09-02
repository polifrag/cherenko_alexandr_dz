# dz_1_3
percents = ['процент','процента','процентов']
percent = 0
for i in range(1,101,1):
    if i>=10 and i<=20:
        percent = percents[2]
    elif i % 10 == 1:
        percent = percents[0]
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        percent = percents[1]
    else:
        percent = percents[2]
    print(i,percent)
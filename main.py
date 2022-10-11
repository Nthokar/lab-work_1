import gspread
import numpy as np

import exercise

gc = gspread.service_account(filename='unitydatasience-365208-a1f90a601085.json')
sh = gc.open("UnitySheets")
price = np.random.randint(2000,10000,11)
mon = list(range(1,11))
i = 0
# while i < len(mon):
#     i += 1
#     if i == 0:
#         continue
#     else:
#         tempInf = ((price[i-1]-price[i-2])/price[i-2])*100
#         tempInf = str(tempInf)
#         tempInf = tempInf.replace('.', ',')
#         sh.sheet1.update(('A' + str(i)), str(i))
#         sh.sheet1.update(('B' + str(i)), str(price[i-1]))
#         sh.sheet1.update(('C' + str(i)), str(tempInf))
#         print(tempInf)
i, j = 1, 0
j_max = 0
iteration = 10000
data = exercise.generate(iteration)
while i < iteration:
    if i == 0:
        continue
    try:
        sh.sheet1.update(('A' + str(i)), str(data[i][0][0]))
        sh.sheet1.update(('B' + str(i)), str(data[i][1][0]))
        sh.sheet1.update(('C' + str(i)), str(data[i][2]))
        print(f"{i} package out")
        i += 1
        j = 0
    except:
        print(f"somting went wrong{j}")
        if j > j_max:
            j_max = j
        j += 1



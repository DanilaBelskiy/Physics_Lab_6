from data_input import tables
from data_output import table_out_1, table_out_2, table_out_3
from table_print import print_table

# constants -------------------------------

Pi = 3.14
Ra = 0.15
Rv = 2500
D = 0.36/1000
S = Pi * (D/2)**2

#------------------------------------------

helperR1 = 1
helperR2 = 1

for i in range(len(tables)):
    for j in range(len(tables[i])):
        if j > 0:
            data = tables[i][j]
            I = data[0]/1000
            U = data[1]
            if i < 3:
                R = U/I - Ra
                R = round(R, 2)
                table_out_1[helperR1][1] = R
                helperR1 += 1
            else:
                R = U / (I - U/Rv)
                R = round(R, 2)
                table_out_2[helperR2][1] = R
                helperR2 += 1

a = table_out_1[1][1] + table_out_1[2][1] + table_out_1[3][1] + table_out_1[4][1]
table_out_3[1][1] = round((a / 4), 2)
a = table_out_1[5][1] + table_out_1[6][1] + table_out_1[7][1] + table_out_1[8][1]
table_out_3[2][1] = round((a / 4), 2)
a = table_out_1[9][1] + table_out_1[10][1] + table_out_1[11][1] + table_out_1[12][1]
table_out_3[3][1] = round((a / 4), 2)
a = table_out_2[1][1] + table_out_2[2][1] + table_out_2[3][1] + table_out_2[4][1]
table_out_3[4][1] = round((a / 4), 2)
a = table_out_2[5][1] + table_out_2[6][1] + table_out_2[7][1] + table_out_2[8][1]
table_out_3[5][1] = round((a / 4), 2)
a = table_out_2[9][1] + table_out_2[10][1] + table_out_2[11][1] + table_out_2[12][1]
table_out_3[6][1] = round((a / 4), 2)

for i in range(1, len(table_out_3)):
    L = table_out_3[i][0]
    R = table_out_3[i][1]
    table_out_3[i][2] = round((R * S / L), 9)

p1 = (table_out_3[1][2] + table_out_3[2][2] + table_out_3[3][2]) / 3
p2 = (table_out_3[4][2] + table_out_3[5][2] + table_out_3[6][2]) / 3
p1 = round(p1, 9)
p2 = round(p2, 9)

print('Сопротивления для всех измерений:')
print_table(table_out_1)
print()
print_table(table_out_2)
print('Среднее сопротивление и удельное сопротивление:')
print_table(table_out_3)
print('Среднее удельное сопротивление(ответ):')
print(p1, p2)

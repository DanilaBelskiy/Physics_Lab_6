def print_table(array):

    def print_line(length, is_up=None):
        if is_up == True:
            symbol = '¯'
        elif is_up == False:
            symbol = '_'
        else:
            symbol = '-'
        for k in range(length):
            print(symbol, end='')

    string_len = len(array[0])
    column_len = len(array)
    column_wights = []
    table_wight = 1
    max = 0
    for j in range(string_len):
        for i in range(column_len):
            if max < len(str(array[i][j])):
                max = len(str(array[i][j]))
        column_wights.append(max)
    for i in range(len(column_wights)):
        table_wight += column_wights[i]
        table_wight += 1
    print('|', end='')
    print_line(table_wight-2, False)
    print('|', end='')
    print()
    print('|', end='')
    for i in range(column_len):
        for j in range(string_len):
            print(array[i][j], end='')
            for k in range(column_wights[j]-len(str(array[i][j]))):
                print(' ', end='')
            print('|', end='')
        if i < column_len-1:
            print()
            print('|', end='')
            print_line(table_wight-2)
            print('|', end='')
            print()
            print('|', end='')
    print()
    print('|', end='')
    print_line(table_wight-2, True)
    print('|', end='')
    print()

'''
for testing
a = [
    ['I', 'U', 'tester'],
    [97, 0.17, 3],
    [110, 0.20, 4],
    [100, 0.18, 5],
    [105, 0.19, 6]
]

print_table(a)
'''

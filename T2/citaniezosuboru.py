subor = open('subor.txt', 'r')
riadok = subor.readline()
while riadok != '':
    print(riadok, end='')
    riadok = subor.readline()
subor.close()
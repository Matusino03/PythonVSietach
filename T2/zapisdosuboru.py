import os

subor = open('subor.txt', 'w')

subor.write('prvy riadok, ')
subor.write('stale prvy riadok\n')
subor.write('druhy riadok')
subor.close()

# if os.path.exists("subor.txt"):
#    os.remove('subor.txt')
# else:
#    print('subor nie je')

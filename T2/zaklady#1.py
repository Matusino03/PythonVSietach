#komentare su v mriezke (#)

#string bud '' alebo ""
print('Ja som Python')
print()
#oddelujeme ciarkou(v jave pluskom)
print('Vypocet sa rovna = ', 5+2*50)
#zadanie inputu
input('stlac Enter')

#datovy typ sa zadavat nemusi
polomer = 16
p_ = 3.14

#  Typy
#* je nasobenie, ** je mocnina
obvod = 2 * p_ * polomer
obsah = p_ * polomer ** 2
print("obvod je ", obvod)
print("obsah je ", obsah)

#type() = vypise nazov daneho datoveho typu
print(type(123))
print(type(22/7))
print(type(':-)'))
input('stlac enter')

#   Premenne

meno = input('ako sa volas?')
print('ahoj', meno)

cislo_str = input('zadaj cenu vyrobku: ')
cislo = float(cislo_str)
spolu = cislo * 4
print('4 vyrobky stoja ', spolu, 'eur/euro')
print('10 vyrobkov stoji ', 10*float(input('zadaj cenu vyrobku ')), 'eur/euro')

cele_cislo = int(input('zadaj cele cislo '))
vysledok = 4 * cele_cislo
print('Vysledok je: ', vysledok)

#vymenenie hodnot
a = 3.15
b = 'Hello'
a, b = b, a
print('a je ', a)
print('b je ', b)

#viac riadkov v jednej premennej
premenna = 'prvyRiadok\ndruhyRiadok\tretiRiadok'
print(premenna)

#   For
for x in 10, 20, 30, 40, 50:
    print(x)

for x in 5, 7, 11, 12, 13:
    x2 = x **2
    print('druha mocnina', x, 'je', x2)

for pismeno in 'Python':
    print(pismeno*10)

#for s range funkciou
#range striktne pokial
for n in range(6):
    print(n)
print('')

#range od kial po kial
for n in range(5, 11):
    print(n)
print()

#for pre vypis hodnot v rozsahu s krokom 10
for i in range(0, 101, 10):
    print(i)

#   Podmienka

body = int(input('pocet bodov '))
if body >= 90:
    print('za', body, 'je A')
elif body >= 80:
    print('za', body, 'je B')
elif body >= 70:
    print('za', body, 'je C')
elif body >= 60:
    print('za', body, 'je D')
elif body >= 50:
    print('za', body, 'je E')
else:
    print('smola mas Fx')

print('')

#AND
cislo = int(input('cislo delitelne 2 a 5 bez zvysku '))

if cislo % 2 == 0 and cislo % 50 == 0:
    print('cislo', cislo, 'je delitelne 2 a 5 bez zvysku')
else:
    print('cislo', cislo, 'nieje delitelne 2 a 5 bez zvysku')

print('')

#OR
cislo = int(input('cislo delitelne 2 a 5 bez zvysku '))

if cislo % 2 == 0 or cislo % 50 == 0:
    print('cislo', cislo, 'je delitelne 2 alebo 5 bez zvysku')
else:
    print('cislo', cislo, 'nieje delitelne 2 alebo 5 bez zvysku')

#   While

x = 0
while x <= 20:
    print('x = ', x)
    x = x + 1
print('')

i = 1
while i < 21:
    print(i, i + 1)
    i += 1
print('')
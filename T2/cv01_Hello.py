class Greeter:
    #konstruktor
    #self v Pythone == this v Jave a C#
    def __init__(self, meno):
        self._meno = meno
        self._vek = 30

    #metoda
    def pozdrav(self):
        for i in range(0, 10):
            if i % 2 == 0:
                # 2 typy vypisu
                print('Ahoj {0}, mas {1} rokov. Vitaj na PSA v 2023'.format(self._meno, self._vek + i))
                print('Ahoj', self._meno, ', mas ', self._vek, ' rokov. Vitaj na PSA v 2023')


#samotny skript
meno = input('zadaj meno ')

greet = Greeter(meno)
greet.pozdrav()



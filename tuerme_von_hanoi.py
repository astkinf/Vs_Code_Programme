# Tuerme von Hanoi
# Geschrieben von Alicia Stockhausen


def zuege(n):
    anzahlZuege = 2**n-1
    print('\tMovements: {0}'.format(str(anzahlZuege)))


def hanoi(n, start, ziel, hilfe):
    if n == 1:
        print('\tMove disk {0} from tower {1} to tower {2}\n'.format(str(n), start, ziel))
    else:
        hanoi(n-1, start, hilfe, ziel)
        print('\tMove disk {0} from tower {1} to tower {2}\n'.format(str(n), start, ziel))
        hanoi(n-1, hilfe, ziel, start)


def hanoiSpiel(n, start, ziel, hilfe):
    hanoi(n, start, ziel, hilfe)
    print('\n\n--------------------------------------------\n\n\t')
    zuege(n)


tower1 = 'A'
tower2 = 'B'
tower3 = 'C'

print('How many disks should have the tower?')
anzahlScheiben = int(input())
hanoiSpiel(anzahlScheiben, tower1, tower3, tower2)
from random import randint

print('Добро пожаловать в числовую угадайку')


def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100


def max_range():
    while True:
        n = input('\nМаксимальное число? ')
        if not n.isdigit() or int(n) < 1:
            print('Введите целое число больше нуля!')
            continue
        return int(n)


def game(n, q):
    count = 0
    print(f'Введите число от 1 до {q}:')
    while True:
        num = input()
        count += 1
        if not is_valid(num):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        else:
            if int(num) > n:
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif int(num) < n:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif int(num) == n:
                print('Вы угадали, поздравляем!'
                      'Вам потребовалось всего', count, "попыток!")
                break


def start():
    q = max_range()
    game(randint(1, q), q)
    while True:
        print('Отличная игра, еще разок?')
        ans = input('Да(Д) или Yes(Y) если желаете продолжить: ')
        if ans.lower() in ('д', 'да', 'yes', 'y'):
            q = max_range()
            game(randint(1, q), q)
            continue
        else:
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break


start()

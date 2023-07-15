from random import randint


def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100


n = randint(1, 100)
count = 0
print('Добро пожаловать в числовую угадайку')
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
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

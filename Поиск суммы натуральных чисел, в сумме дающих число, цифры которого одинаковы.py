class FindTheNaturalNumber:

    def __init__(self):
        self.menu() # Приветствие
        while True: # Логика всей программы
            programm_choice = input()
            if programm_choice == '1':
                self.find_special_sum_with_given_nubers()
            elif programm_choice == '2':
                self.find_sum_of_numbers()
            elif programm_choice.lower() == 'пока': # Завершение программы
                print('Если буду нужен, ты знаешь, где меня искать ;)')
                break
            else:
                print('К сожалению, такой команды я не знаю :(\n'
                      'Пожалуйста, повтори запрос: 1 или 2')

    def find_special_sum_with_given_nubers(self):
        exitMenu = '' # Создаю условие выхода для метода
        while exitMenu.lower() != 'выход': # Запускаю логику
            print(f'Введи числа (каждое число указывай через Enter, без пробелов), в указанном порядке,' # Задаю все базовые переменные
                  f'чтобы найти подходящие числа:')
            counter = 0
            theNumberOfReps = int(input('Сколько чисел хочешь найти: '))
            startNumber = int(input('С какого числа хочешь начать: '))
            theStep = int(input('С каким шагом: '))
            theSum = 0
            totalSumNumber = startNumber
            print('Подсчитал для тебя числа, вот, смотри:')
            while counter != theNumberOfReps:
                stopTrigger = True # Задаём условие выхода из цикла
                theSum += totalSumNumber # Высчитываем сумму элементов
                firstElem = str(theSum)[0] # Берём первый элемен суммы
                for i in str(theSum): # Запускаю проверку на одинаковые цифры в сумме
                    if i == firstElem:
                        continue
                    else:
                        stopTrigger = False # Если не проходит по условию, сразу выходим из цикла
                        break
                if stopTrigger: # Если проверку прошло, то выводим готовый результат
                    print('_____________')
                    print(f'Число {counter + 1} = {totalSumNumber}')
                    print(f'Сумма чисел от {startNumber} до {totalSumNumber} с шагом {theStep} = {theSum}', end='\n_____________\n')
                    counter += 1
                totalSumNumber += theStep # Переходим на следующее число, чтобы посчитать его сумму
                if theSum > 9999999999: # Задаю ограничение, чтобы программа не смогла работать бесконечно
                    print('К сожалению, я таких больших чисел не знаю :(\n'
                          'Моя зона поиска ограничена.')
                    break
            print('Если хотите выйти, напишите "выход". Если продолжить, то что-либо ещё. ', end='')
            exitMenu = input() # Перезапуск/выход
        self.exit(exitMenu)

    def find_sum_of_numbers(self): # Простой подсчёт
        exitMenu = ''
        while exitMenu.lower() != 'выход':
            while True:
                summ = 0
                range_0 = int(input('Введи первое число.'))
                range_1 = int(input('Введи последнее число.'))
                for i in range(range_0, range_1 + 1, int(input('Введи шаг, для подсчёта.'))):
                    summ += i
                print('Твоя сумма получилось = ', summ)
                break
            print('Если хотите выйти, напишите "выход". Если продолжить, то прсото нажмите Enter.', end='')
            exitMenu = input() # Перезапуск/выход
        self.exit(exitMenu)

    def menu(self): # Главное меню
        print(f'Привет, это меню :)\n'
              f'Я подготовил для тебя 2 программы 0_0 \n'
              f'Ты можешь выбрать 1-ую или 2-ую программу, написав соответствующую цифру:\n'
              f'1. Основная программа поиска натуральных чисел, которые в сумме, с первого по последний,\n'
              f'будут давать число, которое записывается одной и той же цифрой.\n'
              f'2. Просто подсчёт необходимой тебе суммы чисел, от первого до последнего, с заданным тобой шагом.\n'
              f'Если захочешь закончить, то вернись в это меню и напиши "пока".\n'
              f'\n'
              f'А теперь напиши, что хочешь использовать? :P')

    def exit(self, exitMenu): # Проверка на выход
        if exitMenu.lower() == 'выход':
            self.menu()

user = FindTheNaturalNumber()

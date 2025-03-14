import serial
import sys
from serial_port_work import work_with_port

isExit = False
portName = ''
baudRate = 9600
answer = ''

while(isExit != True):
    print('------------------------------------------')
    print(f'Данные для входа: \nИмя порта: {portName} \nСкорость: {baudRate}')
    print('------------------------------------------')
    print(f'Выберите формат действия \n1 - Открыть порт \n2 - Задать имя порта \n3 - задать baudRate \n 0 - Закрыть программу')
    print('------------------------------------------')

    answer = input()
    if answer == '1':
        print('Открытие порта')
        try:
            ser = serial.Serial(
                port=portName,
                baudrate=baudRate,
                timeout=1
            )
            print(f"Подключение к {portName} с частотой {baudRate}")
            work_with_port(ser)
        except Exception as e:
            print(f"Ошибка открытия: {e}")
            # sys.exit(1)
    elif answer == '2':
        portName = input('Введите новое имя порта: ')
    elif answer == '3':
        try:
            baudRate = int(input('Введите новую скорость: '))
        except Exception as e:
            print(f'Ошибка ввода: {e}')
    elif answer == '0':
        print('Конец работы программы')
        sys.exit(0)
    else:
        print('Неверный выбор, попробуйте еще раз')


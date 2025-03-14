import serial
import sys
from serial_port_work import work_with_port
import argparse

def main():
    parser = argparse.ArgumentParser(description='Serial port communication tool')
    parser.add_argument('--port', help='Serial port name (e.g. COM1, /dev/ttyUSB0)')
    parser.add_argument('--baud', type=int, help='Baud rate (e.g. 9600, 115200)')
    args = parser.parse_args()

    isExit = False
    portName = args.port
    print(f'порт: {portName}')
    baudRate = args.baud
    print(f'baudRate: {baudRate}')
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

if __name__ == "__main__":
    main()
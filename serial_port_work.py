import serial

def read_all_data_from_port(ser: serial.Serial)-> str:
    answer = ser.read_all()
    return str(answer)

def send_command_to_port(ser: serial.Serial, command):
    try:
        ser.write(command.encode('ascii') + b'\r\n')
    except Exception as e:
        print(f"Ошибка отправки команды: {e}")
    return

def work_with_port(ser: serial.Serial):
    while True:
        print('------------------------------------------')
        print(f'Начало работы с портом {ser}')
        print('------------------------------------------')
        print(f'Выберите формат действия \n1 - Считать данные \n2 - Отправить команду в порт \n 0 - Вернуться к Настройке порта')
        print('------------------------------------------')
        try:
            command = int(input())
            if command == 1:
                print('Считанные данные:')
                answer = read_all_data_from_port(ser)
                print(f'Считанные данные: {answer}')
            elif command == 2:
                print('Отправка команды в порт')
                port_command = input('Введите команду: ')
                send_command_to_port(ser, port_command)
            elif command == 0:
                print('Возврат в меню настройки порта')
                return
        except Exception as e:
            print(f"Ошибка открытия: {e}")
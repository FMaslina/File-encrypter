import pyAesCrypt
import os


#   Функция дешифрования файла
def decryption(file, password):
    #   Задаем размер буфера
    buffer_size = 512 * 1024

    #   Вызываем метод дешифрования
    pyAesCrypt.decryptFile(str(file),
                           str(os.path.splitext(file)[0]),
                           password,
                           buffer_size)

    #   Для отслеживания результата, выводим дешифрованные файлы
    #   Для кого-то данная строка может показаться непонятной, поэтому объясняю:
    #   os.path задает путь до файла, splitext разделяет путь на имя файла и расширение, [0] берет только имя файла
    print(f"Файл {str(os.path.splitext(file)[0])} дешифрован")

    #   Удаляем изначальный файл
    os.remove(file)


#   Далее создаем функцию сканирования директорий
def walking_by_dirs(dir, password):
    #   Перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        #   Если находим файл, дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        #   Если находим директорию, повторяем цикл для поиска файлов
        else:
            walking_by_dirs(path, password)


password = input('Введите пароль для дешифрования')
dir = input('Введите директорию для дешифрования')
walking_by_dirs(dir, password)
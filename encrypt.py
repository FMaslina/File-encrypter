import pyAesCrypt
import os


#   Функция шифрования файла
def encryption(file, password):
    #   Задаем размер буфера
    buffer_size = 512 * 1024

    #   Вызываем метод шифрования
    pyAesCrypt.encryptFile(str(file),
                           str(file) + ".crp",
                           password,
                           buffer_size)

    #   Для отслеживания результата, выводим зашифрованные файлы
    #   Для кого-то данная строка может показаться непонятной, поэтому объясняю:
    #   os.path задает путь до файла, splitext разделяет путь на имя файла и расширение, [0] берет только имя файла
    print(f"Файл {str(os.path.splitext(file)[0])} зашифрован")

    #   Удаляем изначальный файл
    os.remove(file)


#   Далее создаем функцию сканирования директорий
def walking_by_dirs(dir, password):
    #   Перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        #   Если находим файл, шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        #   Если находим директорию, повторяем цикл для поиска файлов
        else:
            walking_by_dirs(path, password)


password = input('Введите пароль для шифрования')
dir = input('Введите директорию для шифрования')
walking_by_dirs(dir, password)
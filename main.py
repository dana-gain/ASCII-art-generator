#перед началом устанавливаем библиотеку PyFiglet "pip3 install pyfiglet"

import io
from pyfiglet import Figlet
from termcolor import cprint
from config import *

# Создаем ASCII-art из текста

f = Figlet(font='standard')               # Задаем тип шрифта меняя font='твой_шрифт'(Список шрифтов смотрим в "fonts.txt")
ascii_art = f.renderText("RUN!")         # "RUN!" заменить на свою надпись
print(ascii_art)                        

def main():
    cprint(text1, 'red')

if __name__ == "__main__":
    main()

filename = "result.txt"  # Имя файла блокнота

with io.open(filename, "w", encoding="utf-8") as file:
    file.write(ascii_art)

print(colored('''Смотри результат в блокноте.

''' + filename, 'cyan'))

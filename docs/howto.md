# Инструкция по использованию

## Установка

Существует два варианта установки:

- Скачать скомпилированую программу
- Скачать исходный код

В случае если вы скачали скомпилированую программу, переходите к пункту по использованию интерфейса

Если вы решили использовать исходный код воспользуйтесь данными данными ниже шагами

- скачайте исходный код, просто скачав с гитхаба либо клонировав его командой

    `git clone https://github.com/Larionov-VA/PhysicsLabTools.git`

- установите зависимости 

    `pip install -r requirements.txt`

## Использование без интерфейса

Для использования программы без интерфейса запускайте файл `run_PLtools.py` и следуйте инструкциям программы

## Использование интерфейса

Для использования программы с интерфейсом запускайте исполняемый файл `PhysicsLabTools.exe` или файл `main.py`

В левой части интерфейса находится таблица для ваших заначений и поле для ввода с рядом стоящей кнопкой которая изменяет количество значений в таблице.

В центральной части интерфейса находится консоль вывода. В нее выводятся сообщения и значения. Ниже консоли находится кнопка генерации значений. Еще ниже находится блок отвечающий за генерацию .docx файла. В нём находятся 2 поля: первое отвечает за инструментальную погрешность, второе за символ которым называются обрабатываемые значения. Ниже в блоке находится кнопка генерации .docx файла.